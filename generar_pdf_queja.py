#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el dossier formal en PDF: escrito de queja por vulneración de derechos
(CIFP de Avilés, curso 2026-2027).
Ejecutar con: .venv/bin/python generar_pdf_queja.py
"""

import io
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, NextPageTemplate, PageTemplate, Paragraph,
    Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents

OUT = "queja-formal-cifp-aviles.pdf"

AZUL = colors.HexColor("#1F3864")
AZUL_CLARO = colors.HexColor("#D9E2F3")
GRIS = colors.HexColor("#5A5A5A")
GRIS_LINEA = colors.HexColor("#B4B4B4")
GRIS_FONDO = colors.HexColor("#F2F2F2")

PAGE_W, PAGE_H = A4
MARGIN_L = 2.4 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.9 * cm
MARGIN_B = 2.4 * cm

# --------------------------------------------------------------------------
# Estilos
# --------------------------------------------------------------------------
S = {}

S["Body"] = ParagraphStyle(
    "Body", fontName="Times-Roman", fontSize=10.5, leading=15.2,
    alignment=TA_JUSTIFY, spaceAfter=6, textColor=colors.black,
)
S["BodyTight"] = ParagraphStyle("BodyTight", parent=S["Body"], spaceAfter=2)
S["Cita"] = ParagraphStyle(
    "Cita", parent=S["Body"], fontName="Times-Italic", fontSize=9.8, leading=13.6,
    leftIndent=10, rightIndent=6, textColor=colors.HexColor("#333333"), spaceAfter=6,
)
S["H1"] = ParagraphStyle(
    "H1", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=AZUL,
    spaceBefore=20, spaceAfter=10, alignment=TA_LEFT,
)
S["H2"] = ParagraphStyle(
    "H2", fontName="Helvetica-Bold", fontSize=10.2, leading=14, textColor=colors.black,
    spaceBefore=12, spaceAfter=5,
)
S["H1NT"] = ParagraphStyle(
    "H1NT", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=AZUL,
    spaceBefore=20, spaceAfter=10, alignment=TA_LEFT,
)
S["H2NT"] = ParagraphStyle(
    "H2NT", fontName="Helvetica-Bold", fontSize=10.2, leading=14, textColor=colors.black,
    spaceBefore=12, spaceAfter=5,
)
S["H3"] = ParagraphStyle(
    "H3", fontName="Helvetica-BoldOblique", fontSize=9.6, leading=13, textColor=AZUL,
    spaceBefore=9, spaceAfter=4,
)
S["PortadaTitulo"] = ParagraphStyle(
    "PortadaTitulo", fontName="Helvetica-Bold", fontSize=25, leading=31,
    alignment=TA_CENTER, textColor=AZUL,
)
S["PortadaSub"] = ParagraphStyle(
    "PortadaSub", fontName="Times-Italic", fontSize=13, leading=18,
    alignment=TA_CENTER, textColor=colors.black,
)
S["PortadaCentro"] = ParagraphStyle(
    "PortadaCentro", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
    alignment=TA_CENTER, textColor=colors.black,
)
S["PortadaMini"] = ParagraphStyle(
    "PortadaMini", fontName="Helvetica", fontSize=8.6, leading=12,
    alignment=TA_CENTER, textColor=GRIS,
)
S["PortadaPie"] = ParagraphStyle(
    "PortadaPie", fontName="Times-Roman", fontSize=10.5, leading=15,
    alignment=TA_CENTER,
)
S["Etiqueta"] = ParagraphStyle(
    "Etiqueta", fontName="Helvetica-Bold", fontSize=8.2, leading=11,
    alignment=TA_CENTER, textColor=AZUL,
)
S["Cell"] = ParagraphStyle(
    "Cell", fontName="Times-Roman", fontSize=9.2, leading=12.2, alignment=TA_LEFT,
)
S["CellB"] = ParagraphStyle(
    "CellB", fontName="Helvetica-Bold", fontSize=8.6, leading=11.4, alignment=TA_LEFT,
    textColor=colors.white,
)
S["CellLabel"] = ParagraphStyle(
    "CellLabel", fontName="Helvetica-Bold", fontSize=8.4, leading=11.4, alignment=TA_LEFT,
    textColor=AZUL,
)
S["CellSmall"] = ParagraphStyle(
    "CellSmall", parent=S["Cell"], fontSize=8.5, leading=11.4,
)
S["Nota"] = ParagraphStyle(
    "Nota", parent=S["Body"], fontSize=9.2, leading=12.8, textColor=GRIS,
    leftIndent=6, rightIndent=6,
)
S["Check"] = ParagraphStyle(
    "Check", parent=S["Body"], fontSize=10, leading=15.5, leftIndent=14,
    firstLineIndent=-14, spaceAfter=0, alignment=TA_LEFT,
)
S["Lista"] = ParagraphStyle(
    "Lista", parent=S["Body"], leftIndent=14, firstLineIndent=-10, spaceAfter=3,
)
S["Firma"] = ParagraphStyle(
    "Firma", parent=S["Body"], alignment=TA_LEFT, spaceBefore=16,
)
S["TOC0"] = ParagraphStyle(
    "TOC0", fontName="Helvetica-Bold", fontSize=10, leading=17,
    textColor=AZUL, spaceBefore=6,
)
S["TOC1"] = ParagraphStyle(
    "TOC1", fontName="Times-Roman", fontSize=9.8, leading=14.5, leftIndent=14,
    textColor=colors.black,
)

# --------------------------------------------------------------------------
# Utilidades de marcado
# --------------------------------------------------------------------------
def P(text, style="Body"):
    return Paragraph(text, S[style])


def linea_de_puntos(ancho=95):
    return "_" * ancho


def caja(texto, estilo="Cita", fondo=GRIS_FONDO, borde=GRIS_LINEA):
    """Párrafo dentro de una caja gris con filete."""
    t = Table([[Paragraph(texto, S[estilo])]], colWidths=[PAGE_W - MARGIN_L - MARGIN_R])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), fondo),
        ("BOX", (0, 0), (-1, -1), 0.5, borde),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def casilla(lado=3.4 * mm):
    """Cuadro pequeño para marcar, que no se estira con la altura de la fila."""
    t = Table([[""]], colWidths=[lado], rowHeights=[lado])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.7, colors.black)]))
    return t


def con_casillas(textos, estilo="Body", ancho_casilla=9 * mm, espacio=2.6 * mm):
    filas = [[casilla(), Paragraph(t, S[estilo])] for t in textos]
    ancho = PAGE_W - MARGIN_L - MARGIN_R
    t = Table(filas, colWidths=[ancho_casilla, ancho - ancho_casilla])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 0),
        ("RIGHTPADDING", (1, 0), (1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1.0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), espacio),
    ]))
    return t


def tabla_formulario(filas, anchos, alturas=None, cabecera=False):
    data = []
    for i, (a, b) in enumerate(filas):
        if cabecera:
            data.append([Paragraph(a, S["CellB"]), Paragraph(b, S["CellB"])])
        else:
            data.append([Paragraph(a, S["CellLabel"]), Paragraph(b, S["Cell"])])
    t = Table(data, colWidths=anchos, rowHeights=alturas, repeatRows=1 if cabecera else 0)
    estilo = [
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (0, -1), AZUL_CLARO),
    ]
    if cabecera:
        estilo.append(("BACKGROUND", (0, 0), (-1, 0), AZUL))
    t.setStyle(TableStyle(estilo))
    return t


# --------------------------------------------------------------------------
# Plantilla de documento
# --------------------------------------------------------------------------
class Dossier(BaseDocTemplate):
    def __init__(self, filename, total=0, **kw):
        BaseDocTemplate.__init__(
            self, filename, pagesize=A4,
            leftMargin=MARGIN_L, rightMargin=MARGIN_R,
            topMargin=MARGIN_T, bottomMargin=MARGIN_B,
            title="Escrito de queja por vulneración de derechos — CIFP de Avilés",
            author="Documentación para cumplimentar",
            subject="Queja por vulneración de derechos (art. 14, Decreto 249/2007)",
            creator="Plantilla PDF",
            **kw
        )
        self.total_paginas = total

        marco_portada = Frame(
            MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R, PAGE_H - MARGIN_T - MARGIN_B,
            id="portada", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        marco_cuerpo = Frame(
            MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R, PAGE_H - MARGIN_T - MARGIN_B,
            id="cuerpo", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="portada", frames=[marco_portada], onPage=self._portada),
            PageTemplate(id="cuerpo", frames=[marco_cuerpo], onPage=self._cabecera_pie),
        ])

    # encabezado y pie
    def _cabecera_pie(self, canv, doc):
        canv.saveState()
        y_cab = PAGE_H - 1.85 * cm
        canv.setFont("Helvetica", 7.4)
        canv.setFillColor(GRIS)
        canv.drawString(MARGIN_L, y_cab, "CIFP DE AVILÉS  ·  ESCRITO DE QUEJA POR VULNERACIÓN DE DERECHOS")
        canv.drawRightString(PAGE_W - MARGIN_R, y_cab, "CURSO 2026-2027")
        canv.setStrokeColor(GRIS_LINEA)
        canv.setLineWidth(0.6)
        canv.line(MARGIN_L, y_cab - 4, PAGE_W - MARGIN_R, y_cab - 4)

        canv.setFont("Helvetica", 7.4)
        canv.drawString(MARGIN_L, 1.45 * cm, "Documento para cumplimentar  ·  Ejemplar para registro de entrada")
        total = self.total_paginas or doc.page
        canv.drawRightString(PAGE_W - MARGIN_R, 1.45 * cm, "Página %d de %d" % (doc.page, total))
        canv.line(MARGIN_L, 1.78 * cm, PAGE_W - MARGIN_R, 1.78 * cm)
        canv.restoreState()

    def _portada(self, canv, doc):
        canv.saveState()
        # filete superior de doble línea
        canv.setStrokeColor(AZUL)
        canv.setLineWidth(2.0)
        canv.line(MARGIN_L, PAGE_H - 2.1 * cm, PAGE_W - MARGIN_R, PAGE_H - 2.1 * cm)
        canv.setLineWidth(0.7)
        canv.line(MARGIN_L, PAGE_H - 2.35 * cm, PAGE_W - MARGIN_R, PAGE_H - 2.35 * cm)
        # filete inferior
        canv.setLineWidth(0.7)
        canv.line(MARGIN_L, 2.6 * cm, PAGE_W - MARGIN_R, 2.6 * cm)
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            nombre = flowable.style.name
            if nombre in ("H1", "H2"):
                nivel = 0 if nombre == "H1" else 1
                self.notify("TOCEntry", (nivel, flowable.getPlainText(), self.page))


# --------------------------------------------------------------------------
# Contenido
# --------------------------------------------------------------------------
def portada():
    e = []
    e.append(Spacer(1, 1.2 * cm))
    e.append(P("CENTRO INTEGRADO DE FORMACIÓN PROFESIONAL DE AVILÉS", "PortadaCentro"))
    e.append(Spacer(1, 2 * mm))
    e.append(P("PRINCIPADO DE ASTURIAS", "PortadaMini"))
    e.append(Spacer(1, 5.2 * cm))
    e.append(P("ESCRITO DE QUEJA", "PortadaTitulo"))
    e.append(Spacer(1, 2 * mm))
    e.append(P("POR VULNERACIÓN DE DERECHOS", "PortadaTitulo"))
    e.append(Spacer(1, 7 * mm))

    filete = Table([[""]], colWidths=[70 * mm], rowHeights=[1])
    filete.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 1.2, AZUL)]))
    fila = Table([[filete]], colWidths=[PAGE_W - MARGIN_L - MARGIN_R])
    fila.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    e.append(fila)
    e.append(Spacer(1, 8 * mm))
    e.append(P(
        "Al amparo del artículo 14 del Decreto 249/2007, de 26 de septiembre, por el que se regulan "
        "los derechos y deberes del alumnado y las normas de convivencia en los centros docentes no "
        "universitarios sostenidos con fondos públicos del Principado de Asturias, y del artículo 18.2.h) "
        "del Reglamento de Régimen Interior del centro", "PortadaSub"))
    e.append(Spacer(1, 3.6 * cm))

    distintivo = Table([[Paragraph("DOCUMENTACIÓN PARA CUMPLIMENTAR", S["Etiqueta"])],
                        [Paragraph("Curso académico 2026-2027", S["PortadaPie"])]],
                       colWidths=[92 * mm], rowHeights=[8 * mm, 9 * mm])
    distintivo.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, AZUL),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, AZUL),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL_CLARO),
    ]))
    cont = Table([[distintivo]], colWidths=[PAGE_W - MARGIN_L - MARGIN_R])
    cont.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    e.append(cont)

    e.append(Spacer(1, 3.2 * cm))
    e.append(P("Avilés, ______ de ____________________ de 2026", "PortadaPie"))
    return e


def indice():
    e = []
    e.append(Spacer(1, 6 * mm))
    e.append(P("ÍNDICE", "H1NT"))
    toc = TableOfContents(dotsMinLevel=0)
    toc.levelStyles = [S["TOC0"], S["TOC1"]]
    e.append(toc)
    return e


def nota_uso():
    e = []
    e.append(P("I. NOTA DE USO Y ADVERTENCIA", "H1"))
    e.append(P(
        "Este documento es una plantilla de trabajo. Reúne, en un único expediente, el escrito de queja "
        "que se presenta ante la Dirección del centro y los anexos que lo acompañan. Las partes que se "
        "presentan figuran en los apartados III a VI; el apartado VII es una nota informativa de uso "
        "interno y <b>no se entrega con el escrito</b>."))
    e.append(P(
        "No contiene ningún hecho relatado. Todos los espacios subrayados deben cumplimentarse con "
        "hechos propios, ciertos, fechados y verificables. Un escrito que describa conductas sin fecha, "
        "sin testigos y sin documento acreditativo no puede ser investigado y será respondido con "
        "generalidades."))
    e.append(caja(
        "<b>Advertencia.</b> Este documento no constituye asesoramiento jurídico. Antes de presentarlo "
        "debe comprobarse el texto vigente de la normativa citada y del Reglamento de Régimen Interior "
        "del centro. El escrito se formula con respeto a la dignidad de todas las personas y sin ánimo de "
        "prejuzgar la actuación de la persona a la que se refiere, cuya versión debe ser oída antes de "
        "cualquier conclusión."))
    return e


def apartado_instrucciones():
    e = []
    e.append(P("II. INSTRUCCIONES DE CUMPLIMENTACIÓN", "H1"))
    e.append(P(
        "El expediente se compone de un escrito principal y tres anexos. Se recomienda cumplimentarlo "
        "por medios informáticos, imprimirlo y firmarlo de puño y letra."))

    pasos = [
        ("Verificar la identificación.", "El nombre y los apellidos de la persona a la que se refiere la queja deben coincidir exactamente con los que figuran en el horario del grupo o en la información pública del centro. Un error en la identificación permite que el escrito no se tramite."),
        ("Relatar hechos, no valoraciones.", "Cada hecho debe responder a cuatro elementos: quién, cuándo, qué conducta observable y qué prueba o testigo la respalda. Las expresiones como «me tiene manía» o «me humilla» no son hechos: se sustituyen por lo que se dijo, se hizo o se negó, con fecha."),
        ("Un hecho por ficha.", "El Anexo I contiene tres fichas. Si hay más hechos, se fotocopia la ficha y se continúa la numeración. Los hechos se ordenan cronológicamente."),
        ("Marcar solo los derechos afectados.", "El apartado III del escrito contiene una lista de derechos. Deben marcarse únicamente aquellos que guarden relación real con los hechos: invocar todos debilita el escrito."),
        ("Numerar las pruebas.", "Cada documento que se aporte se numera y se relaciona con el hecho concreto que acredita. Se aportan copias; los originales se conservan."),
        ("Firmar todas las hojas.", "Se firma el escrito y cada uno de los anexos que se presenten, y se numera cada folio. Si el escrito lo suscriben varias personas, cada una firma su propia hoja de adhesión (Anexo II)."),
        ("Registrar y conservar resguardo.", "El original se presenta en la Secretaría del centro y se solicita copia sellada y fechada. Si se presenta por el registro electrónico, se conserva el justificante con el número de registro. Sin resguardo no puede acreditarse la presentación ni el inicio del plazo."),
        ("Anotar la fecha de presentación.", "Es el punto de partida del plazo de tres meses para que la Administración resuelva, conforme al artículo 21 de la Ley 39/2015."),
    ]
    for i, (titulo, texto) in enumerate(pasos, 1):
        e.append(P("<b>%d. %s</b> %s" % (i, titulo, texto), "Lista"))

    e.append(Spacer(1, 3 * mm))
    e.append(caja(
        "<b>Advertencia sobre la vía elegida.</b> Este escrito es una queja por vulneración de derechos "
        "(artículo 14 del Decreto 249/2007). Si lo que se discute es una calificación, el cauce es la "
        "reclamación del artículo 6 del mismo Decreto, con un plazo de dos días lectivos; si lo que se "
        "impugna es una corrección o sanción impuesta al alumnado, el cauce es la reclamación del "
        "artículo 43, con el mismo plazo de dos días lectivos. Mezclar las tres vías en un solo escrito "
        "provoca que se pierdan los plazos breves."))
    return e


def escrito():
    e = []
    e.append(P("III. ESCRITO DE QUEJA", "H1"))
    e.append(P(
        "A LA DIRECCIÓN DEL CENTRO INTEGRADO DE FORMACIÓN PROFESIONAL DE AVILÉS", "H2NT"))
    e.append(P(
        "A la atención de la persona titular de la Dirección y, por su conducto, de la Jefatura de "
        "Estudios.", "Nota"))
    e.append(Spacer(1, 3 * mm))

    e.append(P("Datos de la persona interesada", "H3"))
    filas = [
        ("Nombre y apellidos", ""),
        ("DNI / NIE", ""),
        ("Domicilio a efectos de notificaciones", ""),
        ("Correo electrónico", ""),
        ("Teléfono de contacto", ""),
        ("Grupo / ciclo / curso / turno", ""),
        ("Módulo profesional", ""),
    ]
    e.append(tabla_formulario(filas, [58 * mm, PAGE_W - MARGIN_L - MARGIN_R - 58 * mm],
                              alturas=[8.5 * mm] * len(filas)))
    e.append(Spacer(1, 5 * mm))

    e.append(P("I. OBJETO", "H3"))
    e.append(P(
        "Que, al amparo del <b>artículo 14 del Decreto 249/2007, de 26 de septiembre</b>, por el que se "
        "regulan los derechos y deberes del alumnado y las normas de convivencia en los centros docentes "
        "no universitarios sostenidos con fondos públicos del Principado de Asturias, y de los "
        "<b>artículos 18.2.h) y 18.2.i) del Reglamento de Régimen Interior</b> del centro, formula "
        "queja por vulneración de derechos en relación con la actuación de la profesora "
        "<b>Dña. Irene Cid Rico</b>, en el marco del módulo profesional indicado, por los hechos que se "
        "relacionan a continuación."))

    e.append(P("II. HECHOS", "H3"))
    e.append(P(
        "Los hechos se relacionan de forma numerada y cronológica. Su descripción detallada, con "
        "expresión de fechas, personas presentes y medios de prueba, consta en el <b>Anexo I</b>, que "
        "forma parte de este escrito. En este apartado se resume cada hecho en una sola línea."))
    ancho_total = PAGE_W - MARGIN_L - MARGIN_R
    cab = [Paragraph(x, S["CellB"]) for x in ("N.º", "Fecha", "Resumen del hecho")]
    filas_h = [cab] + [[Paragraph("%d.º" % i, S["Cell"]), "", ""] for i in range(1, 7)]
    th = Table(filas_h, colWidths=[12 * mm, 26 * mm, ancho_total - 38 * mm],
               rowHeights=[7 * mm] + [10 * mm] * 6)
    th.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    e.append(th)
    e.append(P(
        "Los hechos descritos no constituyen hechos aislados, sino un patrón de conducta mantenido "
        "durante el período comprendido entre el ____ de ________________ de 2026 y el ____ de "
        "________________ de 2026. <i>(Suprímase este párrafo si los hechos son puntuales.)</i>", "Body"))

    e.append(P("III. DERECHOS QUE SE CONSIDERAN VULNERADOS", "H3"))
    e.append(P(
        "Los hechos descritos afectan, en la medida en que resulten acreditados, a los siguientes "
        "derechos. Márquense únicamente los que correspondan:"))
    derechos = [
        ("[    ]", "<b>Artículo 8 del Decreto 249/2007.</b> Derecho a la identidad, integridad y dignidad personal, "
                   "a la protección contra toda agresión física o moral y a un ambiente de buena convivencia. "
                   "<i>Procede cuando el contenido de la conducta sea trato vejatorio, humillaciones, gritos, "
                   "descalificaciones o aislamiento.</i>"),
        ("[    ]", "<b>Artículo 11 del Decreto 249/2007.</b> Derecho de información y de libertad de expresión: ser "
                   "informado de todo aquello que afecte al alumno y poder manifestar sus opiniones. "
                   "<i>Procede cuando no se informa de criterios, programación o decisiones que afectan al alumno.</i>"),
        ("[    ]", "<b>Artículo 6 del Decreto 249/2007 y artículos 16 y 17 del Real Decreto 659/2023.</b> Derecho a "
                   "una evaluación objetiva y a conocer las decisiones de evaluación, así como a acceder a las "
                   "pruebas y documentos de las evaluaciones realizadas."),
        ("[    ]", "<b>Artículo 18.2.b), c), f), h) e i) del Reglamento de Régimen Interior.</b> Valoración objetiva del "
                   "rendimiento, información sobre los criterios de evaluación y calificación, trato respetuoso y "
                   "no discriminatorio, derecho a presentar reclamaciones y derecho a acceder a las pruebas "
                   "corregidas y a obtener copia."),
        ("[    ]", "<b>Artículo 26 del Reglamento de Régimen Interior.</b> Deberes del profesorado: impartir las "
                   "enseñanzas conforme a las programaciones aprobadas, evaluar con objetividad y transparencia, "
                   "velar por el mantenimiento del orden y la convivencia y cumplir el Reglamento."),
        ("[    ]", "<b>Artículo 6.3.b) y f) de la Ley Orgánica 8/1985, reguladora del Derecho a la Educación.</b> "
                   "Derecho a que se respeten la identidad, integridad y dignidad personales y protección contra "
                   "toda agresión física o moral."),
        ("[    ]", "<b>Artículos 13 y 30 de la Ley 15/2022, de 12 de julio, integral para la igualdad de trato y la "
                   "no discriminación.</b> Cuando se aporten indicios fundados de trato discriminatorio, corresponde "
                   "a quien se le imputa la conducta la aportación de una justificación objetiva y razonable, "
                   "suficientemente probada, de las medidas adoptadas y de su proporcionalidad."),
    ]
    e.append(con_casillas([t for _, t in derechos], estilo="Check", espacio=2.4 * mm))

    e.append(P("IV. PRUEBAS", "H3"))
    e.append(P(
        "Se acompañan los siguientes documentos, que se numeran y se relacionan con los hechos del "
        "Anexo I. Márquense los que se aporten:"))
    pruebas = [
        "Copia de la programación docente del módulo o del extracto de criterios de evaluación y calificación facilitado al inicio de curso.",
        "Copia de las pruebas, correcciones o registros del módulo objeto de la queja.",
        "Correos electrónicos o mensajes de la plataforma corporativa del centro, con fecha.",
        "Partes de incidencia, justificantes o informes que obren en poder del centro.",
        "Capturas de pantalla con fecha visible.",
        "Documentación médica o de otra índole que acredite el efecto sobre la salud, si la hubiera.",
        "Otros documentos que se aportan: ______________________________________________________.",
    ]
    e.append(con_casillas(pruebas, estilo="Check", espacio=1.8 * mm))

    e.append(Spacer(1, 3 * mm))
    e.append(P("Testigos que se proponen", "H3"))
    ancho_total = PAGE_W - MARGIN_L - MARGIN_R
    cab_t = [Paragraph(x, S["CellB"]) for x in ("Nombre y apellidos", "Grupo", "Hecho que presenció")]
    filas_t = [cab_t] + [["", "", ""] for _ in range(3)]
    tt = Table(filas_t, colWidths=[62 * mm, 18 * mm, ancho_total - 80 * mm],
               rowHeights=[7 * mm] + [9.5 * mm] * 3)
    tt.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    e.append(tt)
    e.append(Spacer(1, 2 * mm))
    e.append(P(
        "Asimismo, se propone que se recabe informe del departamento de familia profesional "
        "correspondiente y que se practique cualquier otra diligencia que se estime pertinente para el "
        "esclarecimiento de los hechos, incluida la comparecencia de las personas que se indican como "
        "testigos."))

    e.append(P("V. FUNDAMENTOS", "H3"))
    e.append(P(
        "El artículo 14 del Decreto 249/2007 dispone que «el alumnado o sus padres pueden presentar "
        "quejas ante la persona titular de la dirección del centro por aquellas acciones u omisiones, "
        "que en el ámbito del centro docente, supongan trasgresión de los derechos establecidos en este "
        "Decreto. La persona titular de la dirección, previa audiencia de las personas interesadas y "
        "consulta, en su caso, al Consejo Escolar, adoptará las medidas oportunas conforme a la "
        "normativa vigente»."))
    e.append(P(
        "En el mismo sentido, el artículo 18.2.h) del Reglamento de Régimen Interior reconoce al alumnado "
        "el derecho a presentar reclamaciones y a ejercer los derechos de audiencia y revisión previstos "
        "legalmente, y el artículo 58 del mismo Reglamento somete expresamente la convivencia del centro "
        "a lo dispuesto en el Decreto 249/2007. En un centro integrado de formación profesional, la "
        "consulta al Consejo Escolar prevista en el precepto se entiende referida al Consejo Social "
        "regulado en el artículo 28 del Decreto 8/2015, de 11 de febrero."))
    e.append(P(
        "Procede, por tanto, la apertura del trámite de audiencia y la adopción de las medidas que "
        "resulten procedentes, sin perjuicio de la valoración que el centro realice una vez oída la "
        "persona a la que se refiere la queja."))

    e.append(P("VI. PETICIONES", "H3"))
    peticiones = [
        "Que se tenga por presentada esta queja y se le dé el trámite previsto en el artículo 14 del Decreto 249/2007, con audiencia previa de esta parte y, en su caso, consulta al Consejo Social del centro.",
        "Que se recabe informe de la profesora afectada y del departamento de familia profesional, y que se permita a esta parte ratificar y ampliar el escrito, así como aportar nuevas pruebas.",
        "Que se facilite copia de los documentos que se incorporen al expediente y se informe del estado de tramitación, conforme al artículo 53 de la Ley 39/2015.",
        "Que se adopten las medidas oportunas para corregir los efectos de la situación descrita y para evitar que se repita, incluyendo, si procede, la comunicación a la coordinación de Igualdad, bienestar y convivencia del centro.",
        "Que se conserven los instrumentos de evaluación, registros y documentos relacionados con los hechos hasta que la resolución adquiera firmeza.",
        "Que se notifique por escrito a esta parte la resolución que se dicte y las medidas adoptadas.",
        "Que no se adopte ninguna medida de represalia, directa ni indirecta, por la presentación de esta queja, ni sobre esta parte ni sobre las personas que la respalden.",
    ]
    for i, pet in enumerate(peticiones, 1):
        e.append(P("<b>%d.ª</b> %s" % (i, pet), "Lista"))
        e.append(Spacer(1, 1.8 * mm))

    e.append(Spacer(1, 3 * mm))
    e.append(P("VII. DECLARACIÓN Y ADVERTENCIA", "H3"))
    e.append(P(
        "Declaro que los hechos relatados son ciertos y que me constan directamente, sin perjuicio de "
        "las alegaciones que la persona a la que se refieren pueda formular en el trámite de audiencia."))
    e.append(P(
        "Este escrito se formula con estricto respeto a la dignidad de todas las personas y sin ánimo de "
        "prejuzgar la actuación de la profesora, cuya versión debe ser oída antes de cualquier "
        "conclusión. La finalidad de esta queja es exclusivamente que el centro conozca los hechos, los "
        "investigue y adopte, en su caso, las medidas que correspondan conforme a la normativa vigente."))

    e.append(Spacer(1, 8 * mm))
    e.append(P("En Avilés, a ______ de ____________________ de 2026.", "Body"))
    e.append(Spacer(1, 16 * mm))
    e.append(P("Firmado: ______________________________________", "Body"))
    e.append(Spacer(1, 3 * mm))
    e.append(P(
        "Documentación que se acompaña: Anexo I (relación de hechos y pruebas); Anexo II (relación de "
        "alumnado afectado), si procede; Anexo III (designación de representante), si procede; y copia "
        "del DNI o NIE.", "Nota"))
    return e


def anexo_i():
    e = []
    e.append(P("IV. ANEXO I — RELACIÓN DE HECHOS Y PRUEBAS", "H1"))
    e.append(P(
        "Se cumplimenta una ficha por cada hecho. La descripción debe limitarse a lo observable: qué se "
        "dijo, qué se hizo o qué se negó, con expresión de la fecha y de las personas presentes. En el "
        "campo del espacio se indica si ocurrió en el aula, en el taller, en el laboratorio o durante la "
        "formación en empresa. Los hechos se ordenan cronológicamente."))
    e.append(Spacer(1, 2 * mm))

    for n in (1, 2, 3):
        filas = [
            ("Fecha y hora", ""),
            ("Módulo y espacio", ""),
            ("Personas presentes", ""),
            ("Qué ocurrió (solo lo observable)", ""),
            ("Cómo afectó al alumno o alumna", ""),
            ("Prueba que lo acredita", ""),
        ]
        e.append(KeepTogether([
            P("Ficha núm. %d" % n, "H2NT"),
            tabla_formulario(filas, [55 * mm, PAGE_W - MARGIN_L - MARGIN_R - 55 * mm],
                             alturas=[8 * mm, 8 * mm, 8 * mm, 32 * mm, 22 * mm, 12 * mm]),
        ]))
        e.append(Spacer(1, 6 * mm))

    e.append(P("Criterio de redacción de los hechos", "H2"))
    e.append(P("No es un hecho:"))
    e.append(caja("«Me humilla constantemente y me tiene manía.»"))
    e.append(P("Sí es un hecho:"))
    e.append(caja(
        "«El 3 de noviembre de 2026, en el módulo profesional indicado, al preguntarme por la tarea, "
        "manifestó textualmente: “____________________”. Estaban presentes ____________ y "
        "____________. Ese mismo día no se me permitió entregar la práctica que sí aceptó a otros tres "
        "compañeros, que se identifican en el Anexo II.»"))
    e.append(P(
        "Regla práctica: sujeto, fecha, conducta observable y prueba o testigo. Si un hecho carece de "
        "fecha exacta, se ubica al final del anexo en un apartado de hechos reiterados, indicando el "
        "período aproximado y el patrón observado, sin confundirlo con los hechos fechados."))
    return e


def anexo_ii():
    e = []
    e.append(P("V. ANEXO II — RELACIÓN DE ALUMNADO AFECTADO", "H1"))
    e.append(P(
        "Se cumplimenta únicamente si otras personas desean adherirse a la queja. Cada persona describe "
        "sus propios hechos: una relación de firmas sin relato no acredita nada y debilita el escrito. "
        "Este anexo se fotocopia tantas veces como sea necesario."))
    e.append(Spacer(1, 2 * mm))

    filas = [
        ("Nombre y apellidos", ""),
        ("DNI / NIE", ""),
        ("Grupo / ciclo / curso", ""),
        ("Correo electrónico / teléfono", ""),
    ]
    e.append(tabla_formulario(filas, [58 * mm, PAGE_W - MARGIN_L - MARGIN_R - 58 * mm],
                              alturas=[9 * mm] * len(filas)))
    e.append(Spacer(1, 4 * mm))
    e.append(P("Hechos que me afectan personalmente", "H2"))

    hechos = [["1.º", "", ""], ["2.º", "", ""], ["3.º", "", ""]]
    t = Table([[Paragraph("N.º", S["CellB"]), Paragraph("Fecha", S["CellB"]), Paragraph("Qué ocurrió", S["CellB"])]] +
              [[Paragraph(f, S["Cell"]), "", ""] for f, _, _ in hechos],
              colWidths=[12 * mm, 26 * mm, PAGE_W - MARGIN_L - MARGIN_R - 38 * mm],
              rowHeights=[7 * mm, 20 * mm, 20 * mm, 20 * mm])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))
    e.append(t)
    e.append(Spacer(1, 4 * mm))
    e.append(P("Pruebas que aporto: " + linea_de_puntos(78), "Body"))
    e.append(Spacer(1, 2 * mm))
    e.append(P(
        "Solicito ser tenido por interesado en el procedimiento iniciado por el escrito de queja de "
        "fecha ______ de ________________ de 2026 y que se me notifiquen las actuaciones en el medio "
        "indicado."))
    e.append(Spacer(1, 14 * mm))
    e.append(P("En Avilés, a ______ de ____________________ de 2026.     Firmado: "
               "______________________________", "Body"))
    e.append(Spacer(1, 5 * mm))
    e.append(caja(
        "<b>Consentimiento sobre datos personales.</b> Los datos que figuran en esta hoja se facilitan "
        "únicamente a efectos de la tramitación de esta queja por el centro, que actúa como responsable "
        "del tratamiento en el ejercicio de sus funciones educativas (artículo 6.1.e) del Reglamento "
        "General de Protección de Datos). No se autoriza su difusión a terceros ni su publicación."))
    return e


def anexo_iii():
    e = []
    e.append(P("VI. ANEXO III — DESIGNACIÓN DE REPRESENTANTE", "H1"))
    e.append(P(
        "Se cumplimenta únicamente si el escrito lo suscriben varias personas y se desea que las "
        "actuaciones y notificaciones se entiendan con una sola de ellas. Conforme al artículo 7 de la "
        "Ley 39/2015, cuando en un escrito figuren varios interesados, las actuaciones se efectúan con "
        "el representante o el interesado que expresamente se haya señalado y, en su defecto, con el "
        "que figure en primer término."))
    e.append(Spacer(1, 2 * mm))
    e.append(P(
        "Los abajo firmantes, interesados en el procedimiento iniciado por el escrito de queja de fecha "
        "______ de ________________ de 2026, designan como representante a efectos de las actuaciones y "
        "notificaciones a <b>D./Dña.</b> ______________________________________, con DNI/NIE "
        "________________, y autorizan que las comunicaciones se dirijan a la dirección de correo "
        "electrónico ______________________________________."))
    e.append(Spacer(1, 4 * mm))

    cab = [Paragraph(x, S["CellB"]) for x in ("Nombre y apellidos", "DNI / NIE", "Grupo", "Firma")]
    filas = [cab] + [["", "", "", ""] for _ in range(7)]
    t = Table(filas, colWidths=[62 * mm, 28 * mm, 18 * mm, PAGE_W - MARGIN_L - MARGIN_R - 108 * mm],
              rowHeights=[7.5 * mm] + [11 * mm] * 7)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    e.append(t)
    e.append(Spacer(1, 6 * mm))
    e.append(caja(
        "Cada firmante responde de lo que firma. El desistimiento de uno de los interesados afecta "
        "únicamente a quien lo formula, sin perjuicio de la continuación del procedimiento respecto de "
        "los demás."))
    return e


def nota_firmas():
    e = []
    e.append(P("VII. NOTA INFORMATIVA — SOBRE LA NECESIDAD DE RECOGER FIRMAS", "H1"))
    e.append(caja(
        "<b>Documento de uso interno.</b> Esta nota no forma parte del escrito y no se entrega con él. "
        "Se incluye únicamente para orientar la preparación de la queja.", fondo=AZUL_CLARO, borde=AZUL))
    e.append(Spacer(1, 3 * mm))

    e.append(P("1. Conclusión", "H2"))
    e.append(P(
        "No es necesario recoger firmas para presentar la queja, ni existe un número mínimo de alumnos "
        "afectados que la normativa exija. Basta con que la persona que la suscribe sea alumna del "
        "centro y que los hechos afecten a sus derechos. Las firmas no son un requisito de validez: son "
        "un medio de prueba."))

    e.append(P("2. Fundamento", "H2"))
    e.append(P(
        "<b>No hay mínimo legal.</b> El artículo 14 del Decreto 249/2007 no exige número alguno de "
        "alumnos, ni aval de los delegados, ni respaldo de una asociación. La Ley 39/2015 permite que un "
        "escrito lo firmen varios interesados (artículos 5, 7 y 66), sin fijar mínimo ni máximo."))
    e.append(P(
        "<b>La firma identifica, no refuerza.</b> Lo que la firma hace es identificar a la persona "
        "interesada, porque no se admiten quejas anónimas: la Administración exige nombre, apellidos y "
        "firma (artículo 66 de la Ley 39/2015; artículo 17 de la Ley 5/2005 para las quejas ante el "
        "Procurador General)."))
    e.append(P(
        "<b>No confundir con las mayorías del artículo 10.</b> El porcentaje del cinco por ciento del "
        "alumnado o la mayoría absoluta de delegados que recoge el artículo 10 del Decreto 249/2007 se "
        "refiere exclusivamente a la propuesta de inasistencia a clase por discrepancia con decisiones "
        "educativas, y no a la presentación de quejas. Una inasistencia mal convocada puede dar lugar a "
        "una corrección disciplinaria."))

    e.append(P("3. Para qué sirven las firmas", "H2"))
    e.append(P(
        "Para acreditar un patrón de conducta, no una suma de opiniones. Varios relatos independientes, "
        "fechados y coincidentes convierten la versión de un alumno frente a la de una profesora en un "
        "conjunto de indicios, y los indicios cambian la posición de la Administración. Si además "
        "concurre discriminación, el artículo 30 de la Ley 15/2022 invierte la carga de la prueba: "
        "aportados indicios fundados, corresponde a quien se le imputa la conducta justificar de forma "
        "objetiva sus decisiones."))
    e.append(P("Para que las adhesiones sumen y no resten deben cumplirse tres condiciones:"))
    for txt in [
        "1.ª Cada firmante describe sus propios hechos, con fechas. Una lista de nombres sin relato permite responder que la queja es genérica.",
        "2.ª Cada firmante se identifica con nombre, apellidos, DNI y grupo, y firma su propia hoja. No son admisibles las firmas por persona interpuesta.",
        "3.ª Nadie firma bajo presión. El desistimiento posterior de un firmante solo le afecta a él, pero el deterioro del clima del grupo afecta a todos.",
    ]:
        e.append(P(txt, "Lista"))

    e.append(P("4. Cómo comprobar si hay más alumnos afectados", "H2"))
    for txt in [
        "Conversaciones individuales y privadas, sin convocatorias colectivas ni grupos de mensajería sobre el asunto: las capturas de esos grupos acaban con frecuencia en el expediente y fuera de contexto.",
        "Preguntar por hechos concretos y fechados, no por opiniones. La pregunta útil es qué ocurrió y qué día, no si se comparte el malestar.",
        "Pedir a cada persona que redacte su propio relato en el Anexo II, en su domicilio, y que lo firme si desea adherirse. Quien no quiera firmar puede constar como testigo en el escrito principal: resulta más fácil afirmar «lo vi» que «me pasó».",
        "No recoger firmas en clase, en el taller ni durante la jornada, ni circular documentos por la plataforma del centro.",
        "No prometer resultados. Ninguna persona puede garantizar la decisión del centro, y quien se sienta defraudado se convertirá en el primer problema del expediente.",
    ]:
        e.append(P("• " + txt, "Lista"))

    e.append(P("5. Escenarios", "H2"))
    esc = [
        ("Afecta a una sola persona", "Queja individual: escrito y Anexo I. Es la vía más rápida y la que genera menos exposición."),
        ("Varias personas con hechos distintos y fechados", "Dos opciones: una queja por persona presentada el mismo día, o una queja única con Anexo II y Anexo III. La primera genera varios procedimientos y resulta más difícil de archivar en bloque; la segunda es más ordenada."),
        ("Se desea que conste como problema del grupo", "Puede indicarse que los hechos afectan a varios alumnos del grupo y aportar las adhesiones, pero conviene no presentar el escrito como una denuncia de la clase entera: si algunos firmantes se retiran, el escrito queda desautorizado."),
        ("Hay indicios de discriminación o de acoso", "Queja individual, Anexo II, invocación expresa de la Ley 15/2022, comunicación a la coordinación de Igualdad, bienestar y convivencia y copia a la Inspección Educativa."),
    ]
    data = [[Paragraph("Situación", S["CellB"]), Paragraph("Actuación recomendada", S["CellB"])]]
    for a, b in esc:
        data.append([Paragraph(a, S["CellLabel"]), Paragraph(b, S["CellSmall"])])
    t = Table(data, colWidths=[48 * mm, PAGE_W - MARGIN_L - MARGIN_R - 48 * mm])
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.45, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("BACKGROUND", (0, 1), (0, -1), AZUL_CLARO),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    e.append(Spacer(1, 1 * mm))
    e.append(t)

    e.append(P("6. Riesgos que deben evitarse", "H2"))
    for txt in [
        "<b>Difundir el escrito</b> por redes sociales, grupos o tablones. Puede constituir intromisión en el honor o en la protección de datos y desplaza el foco: quien denuncia pasa a ser expedientado. El artículo 59.1.f) y h) del Reglamento tipifica el trato incorrecto y la grabación o difusión de imágenes sin consentimiento.",
        "<b>Incluir hechos no acreditados.</b> Un solo dato falso desacredita todo el escrito y puede tener consecuencias para quien lo firma.",
        "<b>Grabar</b> conversaciones o clases sin consentimiento: el artículo 59.1.h) del Reglamento lo considera conducta contraria a las normas de convivencia.",
        "<b>Dejar de asistir a clase o de entregar tareas</b> mientras se tramita la queja: genera correcciones que contaminan el procedimiento.",
        "<b>Firmar sin leer.</b> Cada firmante responde del contenido de lo que firma.",
    ]:
        e.append(P("• " + txt, "Lista"))
    return e


def checklist():
    e = []
    e.append(P("VIII. LISTA DE VERIFICACIÓN PREVIA AL REGISTRO", "H1"))
    items = [
        "Nombre y apellidos de la profesora verificados con el horario del grupo o la información pública del centro.",
        "Hechos numerados, fechados y redactados sin adjetivos, con testigos o documentos.",
        "Derechos invocados marcados únicamente entre los que guardan relación con los hechos.",
        "Pruebas ordenadas, numeradas y coincidentes con la lista del apartado IV del escrito.",
        "Peticiones concretas y realizables.",
        "Lugar, fecha y firma en el escrito y en cada anexo.",
        "Copia completa del expediente conservada por la persona interesada.",
        "Original presentado en la Secretaría del centro con sello y fecha, o justificante del registro electrónico.",
        "Correo de cortesía al tutor o tutora y a la Jefatura de Estudios anunciando la presentación (recomendable, no obligatorio).",
        "Fecha de presentación anotada: inicia el plazo de tres meses para resolver.",
    ]
    e.append(con_casillas(items, estilo="Check", espacio=2.8 * mm))

    e.append(Spacer(1, 6 * mm))
    e.append(P("Registro interno", "H2"))
    filas = [
        ("Fecha de presentación", ""),
        ("Órgano y persona que la recibe", ""),
        ("Número de registro o de resguardo", ""),
        ("Copia sellada obtenida (sí / no)", ""),
        ("Observaciones", ""),
    ]
    e.append(tabla_formulario(filas, [62 * mm, PAGE_W - MARGIN_L - MARGIN_R - 62 * mm],
                              alturas=[9 * mm, 9 * mm, 9 * mm, 9 * mm, 22 * mm]))
    return e


def normativa():
    e = []
    e.append(P("IX. CUADRO DE NORMATIVA CITADA", "H1"))
    e.append(P(
        "Se recogen únicamente los preceptos invocados en este expediente, con indicación de su "
        "contenido en relación con la queja."))
    filas = [
        ("Constitución Española", "arts. 14, 20, 24, 27 y 29", "Igualdad, libertad de expresión, tutela judicial efectiva, derecho a la educación y derecho de petición."),
        ("Ley Orgánica 8/1985 (LODE)", "art. 6.3.b) y f)", "Derechos básicos del alumnado: respeto a la identidad, integridad y dignidad personales; protección contra toda agresión física o moral."),
        ("Ley Orgánica 3/2022", "—", "Ordenación e integración del Sistema de Formación Profesional."),
        ("Real Decreto 659/2023", "arts. 16 y 17", "Derecho a una evaluación objetiva y derecho a conocer las decisiones de evaluación y a acceder a los documentos y pruebas de las evaluaciones."),
        ("Ley 39/2015", "arts. 5, 7, 21, 24, 53 y 66", "Representación, pluralidad de interesados, obligación de resolver en tres meses, silencio, derechos del interesado y requisitos de los escritos."),
        ("Ley 15/2022", "arts. 13 y 30", "Igualdad de trato en la educación y reglas sobre la carga de la prueba cuando se aportan indicios fundados de discriminación."),
        ("Decreto 249/2007", "art. 6", "Derecho a la valoración objetiva del rendimiento y procedimiento de reclamación contra calificaciones."),
        ("Decreto 249/2007", "art. 8", "Derecho a la identidad, integridad y dignidad personales y a un ambiente de buena convivencia."),
        ("Decreto 249/2007", "art. 11", "Derecho de información y de libertad de expresión."),
        ("Decreto 249/2007", "art. 14", "Quejas ante la Dirección del centro por acciones u omisiones que vulneren los derechos del alumnado; audiencia previa y adopción de medidas."),
        ("Decreto 249/2007", "art. 43", "Reclamación contra las correcciones educativas: dos días lectivos, resolución en tres días lectivos."),
        ("Decreto 249/2007", "art. 49", "Recurso de alzada ante la Consejería en el plazo de un mes."),
        ("Decreto 8/2015", "art. 28", "Consejo Social de los centros integrados de formación profesional: composición y funciones de participación."),
        ("Ley 5/2005", "art. 17", "Forma y características de las quejas ante el Procurador General: por escrito, firmadas y en el plazo de un año."),
        ("RRI del centro, curso 2026-2027", "arts. 18.2.b), c), f), h) e i)", "Derechos del alumnado: valoración objetiva, información sobre criterios, trato respetuoso, reclamaciones y acceso a las pruebas corregidas."),
        ("RRI del centro, curso 2026-2027", "art. 26", "Deberes del profesorado: programación, evaluación objetiva y transparencia, convivencia y cumplimiento del Reglamento."),
        ("RRI del centro, curso 2026-2027", "art. 58", "Sumisión expresa de la convivencia y la disciplina al Decreto 249/2007."),
    ]
    data = [[Paragraph("Norma", S["CellB"]), Paragraph("Precepto", S["CellB"]), Paragraph("Contenido", S["CellB"])]]
    for a, b, c in filas:
        data.append([Paragraph(a, S["CellSmall"]), Paragraph(b, S["CellSmall"]), Paragraph(c, S["CellSmall"])])
    t = Table(data, colWidths=[38 * mm, 30 * mm, PAGE_W - MARGIN_L - MARGIN_R - 68 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
    ]))
    e.append(t)
    return e


def vias():
    e = []
    e.append(P("X. VÍAS POSTERIORES Y PLAZOS", "H1"))
    e.append(P(
        "La queja por vulneración de derechos no tiene un plazo de caducidad específico, pero cuanto "
        "más se tarde más difícil resulta acreditar los hechos. Una vez presentada, el orden de las vías "
        "posteriores es el siguiente."))
    filas = [
        ("Queja ante la Dirección (art. 14)", "Dirección del centro", "Sin plazo específico", "Tres meses; silencio estimatorio con carácter general"),
        ("Reclamación de calificación (art. 6)", "Dirección, por la Secretaría", "Dos días lectivos", "Resolución tras informe del departamento"),
        ("Recurso de alzada (art. 6.10 y 49)", "Consejería de Educación", "Un mes", "Con informe preceptivo de la Inspección Educativa; pone fin a la vía administrativa"),
        ("Reclamación contra una corrección (art. 43)", "Quien la impuso", "Dos días lectivos", "Tres días lectivos; el silencio desestima"),
        ("Inspección Educativa", "Servicio de Inspección", "Sin plazo específico", "Tres meses"),
        ("Procurador General", "Defensor del Pueblo asturiano", "Un año desde el conocimiento de los hechos", "Variable; queja gratuita y no anónima"),
        ("Vía contencioso-administrativa", "Juzgado de lo Contencioso-Administrativo", "Dos meses desde la notificación", "Previa interposición de la vía administrativa"),
    ]
    data = [[Paragraph(x, S["CellB"]) for x in ("Vía", "Órgano", "Plazo para presentarla", "Observaciones")]]
    for a, b, c, d in filas:
        data.append([Paragraph(a, S["CellSmall"]), Paragraph(b, S["CellSmall"]),
                     Paragraph(c, S["CellSmall"]), Paragraph(d, S["CellSmall"])])
    t = Table(data, colWidths=[46 * mm, 36 * mm, 34 * mm, PAGE_W - MARGIN_L - MARGIN_R - 116 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, GRIS_LINEA),
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
    ]))
    e.append(t)
    e.append(Spacer(1, 5 * mm))
    e.append(caja(
        "Los plazos de dos días lectivos son de caducidad y no admiten prórroga: si lo que se discute "
        "es una nota o una sanción, la queja general no interrumpe ni sustituye esos plazos. En caso de "
        "duda sobre qué vía procede, se recomienda presentar el escrito dentro del plazo más breve y "
        "plantear después la queja general."))
    e.append(Spacer(1, 8 * mm))
    e.append(HRFlowable(width="40%", thickness=0.6, color=AZUL, hAlign="CENTER"))
    e.append(Spacer(1, 4 * mm))
    e.append(P("Documento preparado el 10 de noviembre de 2026. No constituye asesoramiento jurídico.", "Nota"))
    return e


def build_story():
    e = [NextPageTemplate("cuerpo")]
    e += portada()
    e.append(NextPageTemplate("cuerpo"))
    e.append(PageBreak())
    e += indice()
    e.append(PageBreak())
    e += nota_uso()
    e += apartado_instrucciones()
    e.append(PageBreak())
    e += escrito()
    e.append(PageBreak())
    e += anexo_i()
    e.append(PageBreak())
    e += anexo_ii()
    e.append(PageBreak())
    e += anexo_iii()
    e.append(PageBreak())
    e += nota_firmas()
    e.append(PageBreak())
    e += checklist()
    e.append(PageBreak())
    e += normativa()
    e.append(PageBreak())
    e += vias()
    return e


def construir(destino, total=0):
    doc = Dossier(destino, total=total)
    doc.multiBuild(build_story())
    return doc


def main():
    buffer = io.BytesIO()
    doc = construir(buffer, total=0)
    total = doc.page
    # segunda pasada con el total ya conocido
    for _ in range(3):
        buffer = io.BytesIO()
        doc = construir(buffer, total=total)
        if doc.page == total:
            break
        total = doc.page
    with open(OUT, "wb") as fh:
        fh.write(buffer.getvalue())
    print("Generado %s — %d páginas" % (OUT, total))


if __name__ == "__main__":
    main()
