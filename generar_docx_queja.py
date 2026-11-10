#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera la versión Word (.docx) del dossier de queja, reutilizando el contenido
del generador del PDF (generar_pdf_queja.py).

Ejecutar: .venv/bin/python generar_docx_queja.py
"""

import re
import generar_pdf_queja as G

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

from reportlab.platypus import (
    Paragraph as RLPara, Table as RLTable, Spacer, PageBreak, KeepTogether,
    HRFlowable,
)

OUT = "queja-formal-cifp-aviles.docx"

AZUL = RGBColor(0x1F, 0x38, 0x64)
GRIS = RGBColor(0x5A, 0x5A, 0x5A)
GRIS_HEX = "B4B4B4"
AZUL_HEX = "1F3864"
AZUL_CLARO_HEX = "D9E2F3"
GRIS_FONDO_HEX = "F2F2F2"

ANCHO_UTIL_CM = 21.0 - 2.4 - 2.2   # 16,4 cm

TAGS = re.compile(r"(</?b>|</?i>)")


# --------------------------------------------------------------------------
# utilidades XML
# --------------------------------------------------------------------------
def sombrear_celda(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    tcPr.append(shd)


def bordes_tabla(table, color=GRIS_HEX, sz="4"):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for borde in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:%s" % borde)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)


def layout_fijo(table):
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)


def bordes_parrafo(par, lados=("top", "bottom"), size="6", color=AZUL_HEX, espacio="4"):
    pPr = par._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for lado in lados:
        el = OxmlElement("w:%s" % lado)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), size)
        el.set(qn("w:space"), espacio)
        el.set(qn("w:color"), color)
        pBdr.append(el)
    pPr.append(pBdr)


def sombrear_parrafo(par, color_hex):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    pPr.append(shd)


def campo(par, instruccion, resultado="1"):
    """Inserta un campo de Word (PAGE, NUMPAGES, TOC...)."""
    r1 = par.add_run()
    f1 = OxmlElement("w:fldChar")
    f1.set(qn("w:fldCharType"), "begin")
    r1._r.append(f1)

    r2 = par.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = instruccion
    r2._r.append(it)

    r3 = par.add_run()
    f2 = OxmlElement("w:fldChar")
    f2.set(qn("w:fldCharType"), "separate")
    r3._r.append(f2)

    par.add_run(resultado)

    r5 = par.add_run()
    f3 = OxmlElement("w:fldChar")
    f3.set(qn("w:fldCharType"), "end")
    r5._r.append(f3)


def actualizar_campos(doc):
    settings = doc.settings.element
    uf = OxmlElement("w:updateFields")
    uf.set(qn("w:val"), "true")
    settings.append(uf)


# --------------------------------------------------------------------------
# runs con negrita y cursiva
# --------------------------------------------------------------------------
def add_runs(par, texto, size=None, bold=False, italic=False, color=None, font=None):
    negrita, cursiva = bold, italic
    for token in TAGS.split(texto):
        if token == "<b>":
            negrita = True
            continue
        if token == "</b>":
            negrita = bold
            continue
        if token == "<i>":
            cursiva = True
            continue
        if token == "</i>":
            cursiva = italic
            continue
        if not token:
            continue
        run = par.add_run(token)
        run.bold = negrita
        run.italic = cursiva
        if size:
            run.font.size = Pt(size)
        if color is not None:
            run.font.color.rgb = color
        if font:
            run.font.name = font
    return par


# --------------------------------------------------------------------------
# estilos
# --------------------------------------------------------------------------
def preparar_estilos(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10.5)
    rpr = normal.element.get_or_add_rPr()
    rFonts = rpr.get_or_add_rFonts()
    rFonts.set(qn("w:eastAsia"), "Times New Roman")
    rFonts.set(qn("w:cs"), "Times New Roman")
    pf = normal.paragraph_format
    pf.space_after = Pt(6)
    pf.line_spacing = 1.15

    for nombre, size, color, italic in (
        ("Heading 1", 13, AZUL, False),
        ("Heading 2", 10.5, RGBColor(0, 0, 0), False),
        ("Heading 3", 9.8, AZUL, True),
    ):
        st = doc.styles[nombre]
        st.font.name = "Arial"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.italic = italic
        st.font.color.rgb = color
        r = st.element.get_or_add_rPr()
        rf = r.get_or_add_rFonts()
        rf.set(qn("w:ascii"), "Arial")
        rf.set(qn("w:hAnsi"), "Arial")
        rf.set(qn("w:eastAsia"), "Arial")
        rf.set(qn("w:cs"), "Arial")
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.space_before = Pt(16 if nombre == "Heading 1" else 12)
        st.paragraph_format.space_after = Pt(8 if nombre == "Heading 1" else 4)


# --------------------------------------------------------------------------
# conversión de flowables de ReportLab a Word
# --------------------------------------------------------------------------
ESTILO_H = {"H1": "Heading 1", "H2": "Heading 2", "H3": "Heading 3"}


def emitir_parrafo(flow, doc):
    nombre = flow.style.name
    texto = flow.text

    if nombre in ESTILO_H:
        par = doc.add_paragraph(style=ESTILO_H[nombre])
        add_runs(par, texto)
        return par

    par = doc.add_paragraph()

    if nombre in ("H1NT", "H2NT"):
        pf = par.paragraph_format
        pf.space_before = Pt(16 if nombre == "H1NT" else 12)
        pf.space_after = Pt(8 if nombre == "H1NT" else 4)
        pf.keep_with_next = True
        add_runs(par, texto, size=13 if nombre == "H1NT" else 10.5,
                 bold=True, color=AZUL if nombre == "H1NT" else RGBColor(0, 0, 0),
                 font="Arial")
        return par

    if nombre == "Cita":
        pf = par.paragraph_format
        pf.left_indent = Cm(0.35)
        pf.right_indent = Cm(0.2)
        pf.space_after = Pt(6)
        add_runs(par, texto, size=9.8, italic=True, color=RGBColor(0x33, 0x33, 0x33))
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        return par

    if nombre == "Nota":
        pf = par.paragraph_format
        pf.left_indent = Cm(0.2)
        pf.space_after = Pt(4)
        add_runs(par, texto, size=9.2, color=GRIS)
        return par

    if nombre == "Lista":
        pf = par.paragraph_format
        pf.left_indent = Cm(0.55)
        pf.first_line_indent = Cm(-0.4)
        pf.space_after = Pt(3)
        add_runs(par, texto)
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        return par

    # cuerpo y variantes
    add_runs(par, texto)
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if nombre == "BodyTight":
        par.paragraph_format.space_after = Pt(2)
    return par


def texto_de_celda(valor):
    if valor is None:
        return "", False
    if isinstance(valor, RLTable):
        return "\u2610", False
    if isinstance(valor, RLPara):
        etiqueta = valor.style.name
        return valor.text, etiqueta
    return str(valor), False


def emitir_caja(tabla, doc):
    """Tabla 1x1: se convierte en párrafo destacado con fondo y filete."""
    valor = tabla._cellvalues[0][0]
    texto = valor.text if isinstance(valor, RLPara) else str(valor)
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.2)
    pf.right_indent = Cm(0.2)
    pf.space_before = Pt(4)
    pf.space_after = Pt(8)
    add_runs(par, texto, size=9.8, italic=True, color=RGBColor(0x33, 0x33, 0x33))
    sombrear_parrafo(par, GRIS_FONDO_HEX)
    bordes_parrafo(par, lados=("top", "left", "bottom", "right"), size="4",
                   color=GRIS_HEX, espacio="6")
    return par


def emitir_casillas(tabla, doc):
    """Tabla de dos columnas cuya primera celda es un cuadro: lista de casillas."""
    for fila in tabla._cellvalues:
        texto = fila[1].text if isinstance(fila[1], RLPara) else str(fila[1])
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.75)
        pf.first_line_indent = Cm(-0.55)
        pf.space_after = Pt(6)
        run = par.add_run("\u2610   ")
        run.font.size = Pt(11)
        add_runs(par, texto)
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def emitir_tabla(tabla, doc):
    filas = tabla._cellvalues
    nfilas, ncols = len(filas), len(filas[0])

    if nfilas == 1 and ncols == 1:
        return emitir_caja(tabla, doc)

    if isinstance(filas[0][0], RLTable):
        return emitir_casillas(tabla, doc)

    t = doc.add_table(rows=nfilas, cols=ncols)
    t.alignment = 0  # izquierda
    layout_fijo(t)
    bordes_tabla(t)

    _, etiqueta_cabecera = texto_de_celda(filas[0][0])
    hay_cabecera = etiqueta_cabecera == "CellB"
    _, etiqueta_col0 = texto_de_celda(filas[1][0]) if nfilas > 1 else ("", "")
    col0_etiquetas = etiqueta_col0 == "CellLabel"

    # anchos
    anchos = getattr(tabla, "_argW", None)
    if anchos:
        for idx, ancho_pt in enumerate(anchos):
            ancho_cm = Cm(ancho_pt * 2.54 / 72.0)
            for fila in t.rows:
                fila.cells[idx].width = ancho_cm

    # alturas mínimas
    alturas = getattr(tabla, "_rowHeights", None)
    if alturas:
        for i, alto_pt in enumerate(alturas):
            if i < len(t.rows) and alto_pt:
                t.rows[i].height = Cm(alto_pt * 2.54 / 72.0)
                t.rows[i].height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST

    for i, fila in enumerate(filas):
        for j, valor in enumerate(fila):
            celda = t.cell(i, j)
            par = celda.paragraphs[0]
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.space_before = Pt(1)
            texto, etiqueta = texto_de_celda(valor)
            es_cabecera = hay_cabecera and i == 0
            es_etiqueta = col0_etiquetas and j == 0
            if es_cabecera:
                add_runs(par, texto, size=8.5, bold=True,
                         color=RGBColor(0xFF, 0xFF, 0xFF), font="Arial")
                sombrear_celda(celda, AZUL_HEX)
            elif es_etiqueta:
                add_runs(par, texto, size=8.5, bold=True, color=AZUL, font="Arial")
                sombrear_celda(celda, AZUL_CLARO_HEX)
            else:
                add_runs(par, texto, size=9)
        if hay_cabecera and i == 0:
            trPr = t.rows[0]._tr.get_or_add_trPr()
            th = OxmlElement("w:tblHeader")
            trPr.append(th)

    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def emitir(flow, doc):
    if isinstance(flow, PageBreak):
        doc.add_page_break()
    elif isinstance(flow, KeepTogether):
        for hijo in flow._content:
            emitir(hijo, doc)
    elif isinstance(flow, Spacer):
        return
    elif isinstance(flow, HRFlowable):
        par = doc.add_paragraph()
        bordes_parrafo(par, lados=("bottom",), size="6", color=AZUL_HEX, espacio="1")
    elif isinstance(flow, RLPara):
        emitir_parrafo(flow, doc)
    elif isinstance(flow, RLTable):
        emitir_tabla(flow, doc)


# --------------------------------------------------------------------------
# portada e índice
# --------------------------------------------------------------------------
def portada(doc):
    def linea(texto, size, bold=False, color=None, espacio_antes=0, espacio_despues=0,
              italic=False, font=None, align=WD_ALIGN_PARAGRAPH.CENTER):
        par = doc.add_paragraph()
        par.alignment = align
        pf = par.paragraph_format
        pf.space_before = Pt(espacio_antes)
        pf.space_after = Pt(espacio_despues)
        pf.line_spacing = 1.0
        run = par.add_run(texto)
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        if color is not None:
            run.font.color.rgb = color
        if font:
            run.font.name = font
        return par

    regla = linea("", 6, espacio_antes=0)
    bordes_parrafo(regla, lados=("top",), size="18", color=AZUL_HEX, espacio="1")

    linea("", 10, espacio_antes=30)
    linea("CENTRO INTEGRADO DE FORMACIÓN PROFESIONAL DE AVILÉS", 12, bold=True, font="Arial")
    linea("PRINCIPADO DE ASTURIAS", 8.5, color=GRIS, font="Arial", espacio_antes=4)

    linea("", 12, espacio_antes=110)
    linea("ESCRITO DE QUEJA", 26, bold=True, color=AZUL, font="Arial")
    linea("POR VULNERACIÓN DE DERECHOS", 26, bold=True, color=AZUL, font="Arial",
          espacio_antes=4)

    filete = linea("", 10, espacio_antes=14, espacio_despues=10)
    bordes_parrafo(filete, lados=("bottom",), size="8", color=AZUL_HEX, espacio="1")
    par = filete.paragraph_format
    par.left_indent = Cm(4.5)
    par.right_indent = Cm(4.5)

    linea("Al amparo del artículo 14 del Decreto 249/2007, de 26 de septiembre, por el que se "
          "regulan los derechos y deberes del alumnado y las normas de convivencia en los centros "
          "docentes no universitarios sostenidos con fondos públicos del Principado de Asturias, y "
          "del artículo 18.2.h) del Reglamento de Régimen Interior del centro",
          11, italic=True, espacio_antes=12)

    linea("", 11, espacio_antes=120)

    caja = doc.add_table(rows=2, cols=1)
    caja.alignment = 0
    layout_fijo(caja)
    bordes_tabla(caja, color=AZUL_HEX, sz="8")
    c0 = caja.cell(0, 0)
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0 = p0.add_run("DOCUMENTACIÓN PARA CUMPLIMENTAR")
    r0.bold = True
    r0.font.size = Pt(8.5)
    r0.font.name = "Arial"
    r0.font.color.rgb = AZUL
    sombrear_celda(c0, AZUL_CLARO_HEX)
    c1 = caja.cell(1, 0)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p1.add_run("Curso académico 2026-2027")
    r1.font.size = Pt(10.5)
    for fila in caja.rows:
        fila.cells[0].width = Cm(9.2)
    for fila in caja.rows:
        fila.height = Cm(1.0)
        fila.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST

    linea("", 11, espacio_antes=100)
    linea("Avilés, ________ de ____________________ de 2026", 10.5)
    regla_final = linea("", 6, espacio_antes=10)
    bordes_parrafo(regla_final, lados=("bottom",), size="4", color=AZUL_HEX, espacio="1")


def indice(doc, apartados):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(6)
    pf.space_after = Pt(10)
    run = par.add_run("ÍNDICE")
    run.bold = True
    run.font.size = Pt(13)
    run.font.name = "Arial"
    run.font.color.rgb = AZUL

    # Campo TOC cuyo resultado provisional es la lista de apartados
    par_toc = doc.add_paragraph()
    par_toc.paragraph_format.space_after = Pt(0)
    r1 = par_toc.add_run()
    f1 = OxmlElement("w:fldChar")
    f1.set(qn("w:fldCharType"), "begin")
    r1._r.append(f1)
    r2 = par_toc.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = 'TOC \\o "1-2" \\h \\z \\u'
    r2._r.append(it)
    r3 = par_toc.add_run()
    f2 = OxmlElement("w:fldChar")
    f2.set(qn("w:fldCharType"), "separate")
    r3._r.append(f2)

    ultimo = par_toc
    for titulo in apartados:
        ultimo = doc.add_paragraph()
        ultimo.paragraph_format.space_after = Pt(7)
        ultimo.paragraph_format.space_before = Pt(3)
        run = ultimo.add_run(titulo)
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = "Arial"
        run.font.color.rgb = AZUL
    fin = ultimo.add_run()
    f3 = OxmlElement("w:fldChar")
    f3.set(qn("w:fldCharType"), "end")
    fin._r.append(f3)

    nota = doc.add_paragraph()
    nota.paragraph_format.space_before = Pt(14)
    r = nota.add_run("Nota: si el índice aparece desactualizado, haga clic sobre él y pulse F9 "
                     "(o botón derecho, «Actualizar campo»).")
    r.font.size = Pt(8.5)
    r.font.color.rgb = GRIS
    r.italic = True


# --------------------------------------------------------------------------
# cabecera y pie
# --------------------------------------------------------------------------
def cabecera_pie(seccion, doc):
    seccion.header.is_linked_to_previous = False
    seccion.footer.is_linked_to_previous = False

    hp = seccion.header.paragraphs[0]
    hp.paragraph_format.tab_stops.add_tab_stop(Cm(ANCHO_UTIL_CM), WD_TAB_ALIGNMENT.RIGHT)
    r = hp.add_run("CIFP DE AVILÉS  ·  ESCRITO DE QUEJA POR VULNERACIÓN DE DERECHOS\t"
                   "CURSO 2026-2027")
    r.font.size = Pt(7.5)
    r.font.name = "Arial"
    r.font.color.rgb = GRIS
    bordes_parrafo(hp, lados=("bottom",), size="4", color=GRIS_HEX, espacio="4")

    fp = seccion.footer.paragraphs[0]
    fp.paragraph_format.tab_stops.add_tab_stop(Cm(ANCHO_UTIL_CM), WD_TAB_ALIGNMENT.RIGHT)
    r2 = fp.add_run("Documento para cumplimentar  ·  Ejemplar para registro de entrada\tPágina ")
    r2.font.size = Pt(7.5)
    r2.font.name = "Arial"
    r2.font.color.rgb = GRIS
    campo(fp, "PAGE", "1")
    r3 = fp.add_run(" de ")
    r3.font.size = Pt(7.5)
    r3.font.name = "Arial"
    r3.font.color.rgb = GRIS
    campo(fp, "NUMPAGES", "16")
    for run in fp.runs:
        run.font.size = Pt(7.5)
        run.font.name = "Arial"
        run.font.color.rgb = GRIS
    bordes_parrafo(fp, lados=("top",), size="4", color=GRIS_HEX, espacio="4")


# --------------------------------------------------------------------------
# principal
# --------------------------------------------------------------------------
def main():
    doc = Document()
    preparar_estilos(doc)

    sec0 = doc.sections[0]
    sec0.page_width = Cm(21)
    sec0.page_height = Cm(29.7)
    sec0.left_margin = Cm(2.4)
    sec0.right_margin = Cm(2.2)
    sec0.top_margin = Cm(2.9)
    sec0.bottom_margin = Cm(2.4)
    sec0.header_distance = Cm(1.4)
    sec0.footer_distance = Cm(1.2)

    bloques = [
        G.nota_uso,
        G.apartado_instrucciones,
        G.escrito,
        G.anexo_i,
        G.anexo_ii,
        G.anexo_iii,
        G.nota_firmas,
        G.checklist,
        G.normativa,
        G.vias,
    ]
    apartados = [f.text for b in bloques for f in b()
                 if isinstance(f, RLPara) and f.style.name == "H1"]

    portada(doc)

    # nueva sección: índice
    sec1 = doc.add_section(WD_SECTION.NEW_PAGE)
    cabecera_pie(sec1, doc)
    indice(doc, apartados)

    # cuerpo
    doc.add_page_break()
    for i, bloque in enumerate(bloques):
        for flow in bloque():
            emitir(flow, doc)
        if i < len(bloques) - 1:
            doc.add_page_break()

    actualizar_campos(doc)

    props = doc.core_properties
    props.title = "Escrito de queja por vulneración de derechos — CIFP de Avilés"
    props.subject = "Curso 2026-2027"
    props.comments = ("Plantilla para cumplimentar. No contiene hechos. "
                      "No constituye asesoramiento jurídico.")
    props.language = "es-ES"

    doc.save(OUT)
    print("Generado %s" % OUT)


if __name__ == "__main__":
    main()
