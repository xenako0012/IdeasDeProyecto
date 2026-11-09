#!/usr/bin/env python3
"""Genera ideas-proyecto-intermodular.md a partir de ideas.json.

Uso:  python3 generar_md.py
La fuente de verdad es ideas.json: edita ahí y regenera el documento.
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / "ideas.json").read_text(encoding="utf-8"))
OUT = BASE / "ideas-proyecto-intermodular.md"

META = DATA["meta"]
MODULOS = DATA["modulos"]
IDEAS = DATA["ideas"]
RAPIDAS = DATA["ideas_rapidas"]
JUEGOS = [i for i in IDEAS if i.get("categoria") == "juego"]
APPS = [i for i in IDEAS if i.get("categoria") != "juego"]

MOD_BY_ID = {m["id"]: m for m in MODULOS}
FUERTE, OPCIONAL, VACIO = "✔", "~", "–"


def estrellas(n: int) -> str:
    return "●" * n + "○" * (5 - n)


def nivel(texto: str) -> str:
    """Marca la cobertura como fuerte u opcional según el texto."""
    return OPCIONAL if texto.strip().lower().startswith("opcional") else FUERTE


def n_fuertes(idea) -> int:
    return sum(1 for v in idea["cobertura"].values() if v and nivel(v) == FUERTE)


def bullet(items) -> str:
    return "\n".join(f"- {i}" for i in items)


def ficha(idea, num: str, compacta: bool = False) -> list:
    """Devuelve las líneas de la ficha de una idea."""
    f = []
    w = f.append
    w("---")
    w("")
    w(f"### {num} {idea['emoji']} {idea['nombre']}")
    w("")
    w(f"*{idea['eslogan']}*")
    w("")
    w("| | |")
    w("|---|---|")
    w(f"| Dificultad | {estrellas(idea['dificultad'])} ({idea['dificultad']}/5) |")
    w(f"| Esfuerzo estimado | {idea['tiempo']} |")
    w(f"| Bloques cubiertos | {n_fuertes(idea)}/{len(MODULOS)} |")
    w(f"| Etiquetas | {', '.join(idea['tags'])} |")
    w("")
    w("**De qué va.** " + idea["descripcion"])
    w("")
    if not compacta:
        w("**Arquitectura (de un vistazo)**")
        w("")
        w(bullet(idea["arquitectura"]))
        w("")
    w("**Stack sugerido**")
    w("")
    w("| Pieza | Tecnología |")
    w("|-------|------------|")
    for k, v in idea["stack"].items():
        w(f"| {k} | {v} |")
    w("")
    w("**Cómo cubre cada RA**")
    w("")
    w("| Bloque | Cómo lo justificas |")
    w("|--------|--------------------|")
    for mid, m in MOD_BY_ID.items():
        txt = idea["cobertura"].get(mid)
        mark = nivel(txt) if txt else VACIO
        w(f"| {mark} **{m['nombre']}** (`{m['codigo']}`) | {txt or 'No aplica: justifícalo en la memoria.'} |")
    w("")
    w("**Por qué mola**")
    w("")
    w(bullet(idea["mola"]))
    w("")
    w("**Riesgos y cómo mitigarlos**")
    w("")
    w(bullet(idea["riesgos"]))
    w("")
    w("**Alcance por fases (corta aquí si te falta tiempo)**")
    w("")
    w("| Fase | Entregable |")
    w("|------|------------|")
    for fase, items in idea["alcance"].items():
        w(f"| {fase} | {'; '.join(items)} |")
    w("")
    return f


L = []
w = L.append

# ---------------------------------------------------------------- cabecera
w(f"# {META['titulo']}")
w("")
w(f"**{META['ciclo']} · {META['curso']} · última actualización: {META['actualizado']}**")
w("")
w(f"> {META['nota']}")
w("")
w("## Cómo usar este documento")
w("")
w("1. Lee primero la **[guía para juegos en el navegador](#4-juegos-en-el-navegador)**: las reglas del juego aquí son distintas.")
w("2. Compara con la **[matriz de cobertura](#3-matriz-de-cobertura)** qué idea toca cuántos módulos.")
w("3. Lee solo las fichas de las 3-4 ideas que te encajen.")
w("4. Pásales el **[checklist de elección](#8-checklist-de-elección)** antes de decidirte.")
w("5. Si necesitas algo más pequeño, mira las **[ideas rápidas](#7-ideas-rápidas-plan-b)**.")
w("")
w("Tabla de contenidos:")
w("")
w("1. [RA → módulo: qué te van a pedir](#1-ra--módulo-qué-te-van-a-pedir)")
w("2. [Resumen de ideas](#2-resumen-de-ideas)")
w("3. [Matriz de cobertura](#3-matriz-de-cobertura)")
w("4. [Juegos en el navegador](#4-juegos-en-el-navegador)")
w("5. [Otras ideas (por si cambias de rumbo)](#5-otras-ideas-por-si-cambias-de-rumbo)")
w("6. [Recomendación según tu perfil](#6-recomendación-según-tu-perfil)")
w("7. [Ideas rápidas (plan B)](#7-ideas-rápidas-plan-b)")
w("8. [Checklist de elección](#8-checklist-de-elección)")
w("9. [Estructura propuesta de la memoria](#9-estructura-propuesta-de-la-memoria)")
w("10. [Trampas clásicas](#10-trampas-clásicas)")
w("")

# ---------------------------------------------------------------- 1
w("## 1. RA → módulo: qué te van a pedir")
w("")
w("| # | Bloque | Módulo | Resultado de aprendizaje | Qué suele evaluar el tribunal |")
w("|---|--------|--------|--------------------------|-------------------------------|")
for i, m in enumerate(MODULOS, 1):
    ras = "<br>".join(f"· {r}" for r in m["ra"])
    w(f"| {i} | **{m['nombre']}** | `{m['codigo']}` | {ras} | {m['claves']} |")
w("")
w("> `SI-RA6` (seguridad) es un resultado de aprendizaje del módulo de **Sistemas Informáticos**, ")
w("> pero lo he separado en la matriz porque casi siempre se evalúa (y se defiende) aparte.")
w("")

# ---------------------------------------------------------------- 2
w("## 2. Resumen de ideas")
w("")
w("| Tipo | Idea | Qué es | Dificultad | Esfuerzo | Bloques |")
w("|:----:|------|--------|:----------:|:--------:|:-------:|")
for idea in JUEGOS + APPS:
    tipo = "🎮" if idea.get("categoria") == "juego" else "💼"
    w(
        f"| {tipo} | **{idea['nombre']}** | {idea['eslogan']} | "
        f"{estrellas(idea['dificultad'])} ({idea['dificultad']}/5) | {idea['tiempo']} | "
        f"{n_fuertes(idea)}/{len(MODULOS)} |"
    )
w("")

# ---------------------------------------------------------------- 3
w("## 3. Matriz de cobertura")
w("")
w("`✔` = cubre el RA con peso · `~` = lo toca de forma opcional o secundaria · `–` = no aplica o hay que justificarlo")
w("")
for titulo, grupo in (("🎮 Juegos en el navegador", JUEGOS), ("💼 Otras ideas", APPS)):
    w(f"**{titulo}**")
    w("")
    w("| Idea | " + " | ".join(f"`{m['codigo']}`" for m in MODULOS) + " | Total |")
    w("|------|" + "|".join([":-:"] * len(MODULOS)) + "|:-:|")
    for idea in grupo:
        celdas = []
        for mid in MOD_BY_ID:
            txt = idea["cobertura"].get(mid)
            celdas.append(nivel(txt) if txt else VACIO)
        w(f"| {idea['emoji']} {idea['nombre'].split('—')[0].strip()} | " + " | ".join(celdas) + f" | **{n_fuertes(idea)}** |")
    w("")
w("Leyenda de códigos:")
w("")
w("| Código | Significado |")
w("|--------|-------------|")
for m in MODULOS:
    w(f"| `{m['codigo']}` | {m['nombre']} |")
w("")
w("Que una idea sume muchos `✔` no significa que todos los bloques pesen igual: en la ficha de cada idea ")
w("tienes el detalle de **cómo** se justifica cada RA, que es lo que realmente te va a preguntar el tribunal. ")
w("Donde veas `~` o `–`, apunta en la memoria por qué no aplica o cómo lo cubres de forma transversal ")
w("(documentación, despliegue, pruebas, presupuesto).")
w("")

# ---------------------------------------------------------------- 4
w("## 4. Juegos en el navegador")
w("")
w("### 4.0 Antes de elegir: cómo se defiende un juego en un proyecto intermodular")
w("")
w("Un juego es un proyecto **excelente**... siempre que no se quede en 'un canvas con sprites'. ")
w("Estas son las reglas que marcan la diferencia entre un 4 y un 9:")
w("")
w(bullet(DATA["notas_juegos"]))
w("")
w("**Stack orientativo para juegos web**")
w("")
w("| Pieza | Opción recomendada |")
w("|-------|--------------------|")
for k, v in DATA["stack_juegos"].items():
    w(f"| {k} | {v} |")
w("")
for n, idea in enumerate(JUEGOS, 1):
    L.extend(ficha(idea, f"4.{n}"))

# ---------------------------------------------------------------- 5
w("## 5. Otras ideas (por si cambias de rumbo)")
w("")
w("No son juegos, pero están aquí por si en algún momento te replanteas el enfoque y quieres comparar.")
w("")
for n, idea in enumerate(APPS, 1):
    L.extend(ficha(idea, f"5.{n}"))

# ---------------------------------------------------------------- 6
w("## 6. Recomendación según tu perfil")
w("")
nombres = {i["id"]: i["nombre"] for i in IDEAS}
for rec in DATA["recomendaciones"]:
    w(f"**→ {rec['perfil']}: {nombres[rec['pick']]}**")
    w("")
    w(rec["por_que"])
    w("")

# ---------------------------------------------------------------- 7
w("## 7. Ideas rápidas (plan B)")
w("")
w("Proyectos más pequeños por si tu centro te limita el alcance o vas justo de tiempo.")
w("")
w("| Tipo | Idea | Qué aporta | Bloques que cubre |")
w("|:----:|------|------------|-------------------|")
for r in RAPIDAS:
    tipo = "🎮" if r.get("categoria") == "juego" else "💼"
    codes = ", ".join(f"`{MOD_BY_ID[c]['codigo']}`" for c in r["cubre"] if c in MOD_BY_ID)
    w(f"| {tipo} | **{r['nombre']}** | {r['detalle']} | {codes} |")
w("")

# ---------------------------------------------------------------- 8
w("## 8. Checklist de elección")
w("")
w("Antes de cerrar la idea, responde honestamente:")
w("")
for i, c in enumerate(DATA["checklist_eleccion"], 1):
    w(f"{i}. {c}")
w("")

# ---------------------------------------------------------------- 9
w("## 9. Estructura propuesta de la memoria")
w("")
for i, s in enumerate(DATA["estructura_memoria"], 1):
    w(f"{i}. {s}" if not s[0].isdigit() else s)
w("")

# ---------------------------------------------------------------- 10
w("## 10. Trampas clásicas")
w("")
w(bullet(DATA["trampas"]))
w("")
w("---")
w("")
w("¿Quieres que desarrolle una de estas ideas en profundidad (análisis de requisitos, modelo de datos, ")
w("arquitectura, protocolo de red y planificación)? Dime cuál y la convierto en el documento base del proyecto.")
w("")

OUT.write_text("\n".join(L), encoding="utf-8")
print(f"Generado {OUT} ({len(L)} líneas, {len(JUEGOS)} juegos + {len(APPS)} apps)")
