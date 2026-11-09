# IdeasDeProyecto

Recopilación de ideas para el **Proyecto Intermodular** del ciclo de
**Desarrollo de Aplicaciones Multiplataforma (DAM)** — 2º curso.

## Contenido

| Archivo | Qué es |
|---|---|
| [`ideas-proyecto-intermodular.md`](ideas-proyecto-intermodular.md) | El documento principal: 10 ideas desarrolladas + 6 ideas rápidas, con cobertura de cada Resultado de Aprendizaje, stack, riesgos y alcance por fases. |
| [`ideas.json`](ideas.json) | **Fuente de verdad** de todos los datos (ideas, módulos, recomendaciones, checklist). |
| [`generar_md.py`](generar_md.py) | Regenera el Markdown a partir de `ideas.json`. |
| [`visor.html`](visor.html) | Visor web interactivo: filtra ideas por módulo/RA, dificultad y texto, y consulta la matriz de cobertura. |

## Ver el visor en el navegador

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

y abre `http://localhost:8000/visor.html`
(el visor lee `ideas.json` con `fetch`, así que necesita servirse por HTTP;
si abres el HTML a pelo verás un aviso en lugar de las ideas).

## Regenerar el documento

Edita `ideas.json` y después:

```bash
python3 generar_md.py
```

## Cómo está organizada la información

Cada idea indica, bloque a bloque, **cómo** se justifica el RA correspondiente:

| Código | Bloque |
|---|---|
| `SI` | Configuración y explotación de sistemas |
| `SI-RA6` | Seguridad en sistemas, servicios y aplicaciones |
| `BD` | Gestión de bases de datos |
| `ED` | Gestión de entornos de desarrollo |
| `AD` | Acceso a datos |
| `PMDM·M` | Contenidos multimedia |
| `PMDM·MOV` | Dispositivos móviles |
| `DI` | Desarrollo de interfaces |
| `PSP` | Servicios y procesos (multiproceso / multihilo) |
| `SGE` | Sistemas de gestión empresarial (ERP-CRM) |

En la matriz: `✔` = cubre el RA con peso · `~` = opcional o secundario · `–` = no aplica (hay que justificarlo).
