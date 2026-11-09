# Banco de ideas para el Proyecto Intermodular

**Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) · 2º curso · última actualización: 2026-11-09**

> Los Resultados de Aprendizaje (RA) listados en 'modulos' son los que has aportado; el código de módulo es el del currículo LOE de DAM (RD 1584/2011), confírmalo con tu centro por si hay adaptación autonómica.

## Cómo usar este documento

1. Empieza por la **[matriz de cobertura](#3-matriz-de-cobertura)**: qué idea toca cuántos módulos.
2. Lee solo las fichas de las 3-4 ideas que te encajen (sección 4).
3. Pásales el **[checklist de elección](#7-checklist-de-elección)** antes de decidirte.
4. Si necesitas algo más pequeño, mira las **[ideas rápidas (plan B)](#5-ideas-rápidas-plan-b)**.

Tabla de contenidos:

1. [RA → módulo: qué te van a pedir](#1-ra--módulo-qué-te-van-a-pedir)
2. [Resumen de ideas](#2-resumen-de-ideas)
3. [Matriz de cobertura](#3-matriz-de-cobertura)
4. [Fichas detalladas](#4-fichas-detalladas)
5. [Ideas rápidas (plan B)](#5-ideas-rápidas-plan-b)
6. [Recomendación según tu perfil](#6-recomendación-según-tu-perfil)
7. [Checklist de elección](#7-checklist-de-elección)
8. [Estructura propuesta de la memoria](#8-estructura-propuesta-de-la-memoria)
9. [Trampas clásicas](#9-trampas-clásicas)

## 1. RA → módulo: qué te van a pedir

| # | Bloque | Módulo | Resultado de aprendizaje | Qué suele evaluar el tribunal |
|---|--------|--------|--------------------------|-------------------------------|
| 1 | **Configuración y explotación de sistemas** | `SI` | · Configurar y explotar sistemas informáticos, adaptando la configuración lógica del sistema según las necesidades de uso y los criterios establecidos. | Instalación y hardening del SO, servicios (systemd), virtualización/contenedores, copias de seguridad, monitorización, red, despliegue. |
| 2 | **Seguridad en sistemas, servicios y aplicaciones** | `SI-RA6` | · Aplicar técnicas y procedimientos relacionados con la seguridad en sistemas, servicios y aplicaciones, cumpliendo el plan de seguridad. | Autenticación/autorización (RBAC, JWT, OAuth2, 2FA), cifrado en tránsito y en reposo, TLS, auditoría, gestión de secretos, endurecimiento, RGPD, copias seguras, plan de seguridad. |
| 3 | **Gestión de bases de datos** | `BD` | · Gestionar bases de datos, interpretando su diseño lógico y verificando integridad, consistencia, seguridad y accesibilidad de los datos. | Diseño lógico y normalización, integridad referencial, transacciones y concurrencia, procedimientos/disparadores, copias y restauración, control de accesos, migraciones. |
| 4 | **Gestión de entornos de desarrollo** | `ED` | · Gestionar entornos de desarrollo adaptando su configuración en cada caso para permitir el desarrollo y despliegue de aplicaciones. | Control de versiones (Git + ramas/issues), IDE y perfiles, automatización de compilación (Maven/Gradle), pruebas, CI/CD, contenedores de desarrollo, empaquetado e instaladores. |
| 5 | **Acceso a datos** | `AD` | · Desarrollar aplicaciones multiplataforma con acceso a bases de datos utilizando lenguajes, librerías y herramientas adecuados a las especificaciones. | Persistencia (ORM o DAO), mapeo objeto-relacional, consumo de APIs/servicios web, serialización, tratamiento de errores, patrones de repositorio. |
| 6 | **Contenidos multimedia** | `PMDM·M` | · Integrar contenidos gráficos y componentes multimedia en aplicaciones multiplataforma, empleando herramientas específicas y cumpliendo los requerimientos establecidos. | Imagen (captura, filtros, OCR, detección), audio y vídeo (captura, códecs, streaming, transcodificación), gráficos 2D/3D, animaciones, generación de PDF/informes. |
| 7 | **Dispositivos móviles** | `PMDM·MOV` | · Desarrollar aplicaciones para teléfonos, PDA y otros dispositivos móviles empleando técnicas y entornos de desarrollo específicos. | Android (Kotlin/Java), ciclo de vida, sensores, cámara, GPS, notificaciones push, persistencia local (Room/SQLite), sincronización offline, permisos y empaquetado. |
| 8 | **Desarrollo de interfaces** | `DI` | · Desarrollar interfaces gráficos de usuario interactivos y con la usabilidad adecuada, empleando componentes visuales estándar o implementando componentes visuales específicos. | JavaFX / Swing / Qt / GTK / web-embebida, eventos, layouts adaptables, componentes personalizados, gráficas, validación, internacionalización, accesibilidad, usabilidad y testing de UI. |
| 9 | **Servicios y procesos (multiproceso / multihilo)** | `PSP` | · Desarrollar aplicaciones multiproceso y multihilo empleando librerías y técnicas de programación específicas. | Hilos y pools, sincronización (locks, semáforos, monitores), productor-consumidor, concurrencia y condiciones de carrera, sockets, RMI/web services, servicios de sistema, señales y procesos. |
| 10 | **Sistemas de gestión empresarial (ERP-CRM)** | `SGE` | · Participar en la implantación de sistemas ERP-CRM evaluando la utilidad de cada uno de sus módulos.<br>· Gestionar la información almacenada en sistemas ERP-CRM garantizando su integridad. | Implantación de Odoo/Dolibarr/ERPNext, parametrización de módulos (ventas, compras, stock, contabilidad, CRM, RRHH), migración e integridad de datos, informes, conexión con tu app vía API. |

> `SI-RA6` (seguridad) es un resultado de aprendizaje del módulo de **Sistemas Informáticos**, 
> pero lo he separado en la matriz porque casi siempre se evalúa (y se defiende) aparte.

## 2. Resumen de ideas

| Idea | Qué es | Dificultad | Esfuerzo | Bloques cubiertos |
|------|--------|:----------:|:--------:|:-----------------:|
| 🎥 **SentinelVIS — Tu propio NVR de videovigilancia IP** | Un servidor multihilo que vigila N cámaras a la vez, entiende lo que ve y te avisa al móvil. | ●●●●● (5/5) | 140-180 h | 9/10 |
| 📦 **LogiScan — Almacén con PDA, códigos de barras y RFID** | El RA dice literalmente 'teléfonos, PDA y otros dispositivos móviles': aquí la PDA es la protagonista. | ●●●●○ (4/5) | 120-160 h | 10/10 |
| 🏋️ **GymCore — ERP-CRM de gimnasio con app de socio y multimedia** | Reservas, acceso por QR, rutinas en vídeo y cuotas facturadas desde el ERP: el pack completo. | ●●●●○ (4/5) | 130-170 h | 10/10 |
| 🛡️ **NetSentinel — Monitorización de red y mini-SOC** | Descubre los equipos de la red, vigílalos a la vez y recibe la alerta antes de que caiga el servicio. | ●●●●○ (4/5) | 110-150 h | 9/10 |
| 🍿 **StreamHub — Servidor multimedia y streaming (estilo Plex propio)** | Transcodifica bajo demanda, lleva el catálogo en la BD y sigue viendo la peli en el móvil donde la dejaste. | ●●●●○ (4/5) | 120-160 h | 9/10 |
| 🚚 **FleetTrack — Flota y reparto con seguimiento GPS en vivo** | Ves los vehículos moverse en el mapa y la prueba de entrega llega con foto, firma y coordenadas. | ●●●●● (5/5) | 140-180 h | 10/10 |
| 🎫 **HelpDesk Pro — Gestión de incidencias con SLA y app de técnico** | Tickets con SLA, técnicos en campo y facturación de horas: el clásico, pero bien hecho. | ●●●○○ (3/5) | 100-140 h | 10/10 |
| 📄 **DocuFlow — Digitalización certificada y gestor documental con OCR** | Escaneas, el OCR indexa solo y cada documento queda trazado, cifrado y firmado. | ●●●●○ (4/5) | 120-160 h | 10/10 |
| 🏠 **EcoDomus — Domótica y control de accesos con Raspberry Pi** | Luces, sensores, cerradura y cámara: todo orquestado por hilos y controlado desde el móvil. | ●●●●● (5/5) | 140-180 h | 9/10 |
| 🍽️ **MesaFácil — Reservas para restaurante o alojamiento rural** | Concurrencia de verdad: dos clientes, la última mesa, una sola reserva. | ●●●○○ (3/5) | 100-140 h | 10/10 |

## 3. Matriz de cobertura

`✔` = cubre el RA con peso · `~` = lo toca de forma opcional o secundaria · `–` = no aplica o hay que justificarlo

| Idea | `SI` | `SI-RA6` | `BD` | `ED` | `AD` | `PMDM·M` | `PMDM·MOV` | `DI` | `PSP` | `SGE` | Total |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 🎥 SentinelVIS | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 📦 LogiScan | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🏋️ GymCore | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🛡️ NetSentinel | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 🍿 StreamHub | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 🚚 FleetTrack | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🎫 HelpDesk Pro | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 📄 DocuFlow | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🏠 EcoDomus | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 🍽️ MesaFácil | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |

Leyenda de códigos:

| Código | Significado |
|--------|-------------|
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

Que una idea sume muchos `✔` no significa que todos los bloques pesen igual: en la ficha de cada idea 
tienes el detalle de **cómo** se justifica cada RA, que es lo que realmente te va a preguntar el tribunal. 
Donde veas `~` o `–`, apunta en la memoria por qué no aplica o cómo lo cubres de forma transversal 
(documentación, despliegue, pruebas, presupuesto).

## 4. Fichas detalladas

---

### 4.1 🎥 SentinelVIS — Tu propio NVR de videovigilancia IP

*Un servidor multihilo que vigila N cámaras a la vez, entiende lo que ve y te avisa al móvil.*

| | |
|---|---|
| Dificultad | ●●●●● (5/5) |
| Esfuerzo estimado | 140-180 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | multimedia, redes, seguridad, escritorio+móvil, visión artificial |

**De qué va.** Servicio que ingesta flujos RTSP/ONVIF de varias cámaras, detecta movimiento y personas con visión artificial, graba solo los eventos relevantes y sirve el vídeo en directo e histórico. Cliente de escritorio con mosaico de cámaras y línea de tiempo de eventos, y app Android con notificaciones push y visor en directo. Todo cerrado con autenticación, RBAC, cifrado de grabaciones y un plan de seguridad real.

**Arquitectura (de un vistazo)**

- Servicio de captura multihilo: un hilo por cámara + pool de workers de inferencia + cola de eventos (productor/consumidor).
- Proceso independiente de grabación que remuxea a MP4/HLS y aplica retención por espacio y antigüedad.
- Servidor de API + WebSocket para directo, eventos y push (FCM).
- Clientes: escritorio (JavaFX o Tauri) y Android (ExoPlayer + miniaturas).
- Postgres + sistema de ficheros indexado para grabaciones; copias programadas y rotadas.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Escritorio | Java 21 + JavaFX (alternativa: Python + PyQt o Tauri) |
| Móvil | Android Kotlin nativo + ExoPlayer + FCM |
| Servicio | Java (ExecutorService, NIO, WebSocket) o Python (asyncio + multiprocessing) |
| Multimedia | OpenCV + FFmpeg + YOLO-nano vía ONNX Runtime |
| Datos | PostgreSQL + Redis (cola de trabajos) |
| Infra | Debian + Docker + systemd + Nginx con TLS + WireGuard |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Despliegue en servidor Linux con systemd, contenedores, almacenamiento y cuotas, VPN de acceso remoto, tareas programadas y monitorización de recursos. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | TLS, JWT + 2FA, RBAC por instalación, cifrado de grabaciones en reposo, registro de auditoría de accesos, endurecimiento del SO, RGPD y cartelería/aviso legal de videovigilancia. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo lógico (instalaciones, cámaras, eventos, grabaciones, roles), integridad referencial, transacciones, política de retención y estrategia de copias y restauración verificada. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Git con ramas e issues, CI con GitHub Actions (build, tests, imagen Docker), entornos dev/test/prod y empaquetado con jpackage o imagen Docker. |
| ✔ **Acceso a datos** (`AD`) | Persistencia de cámaras, eventos, grabaciones y usuarios con JPA/Hibernate o DAO; consultas por rango temporal e índices; exportación de informes. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Ingesta RTSP con FFmpeg, tratamiento de imagen con OpenCV (BackgroundSubtractor, detección de personas), generación de miniaturas, remux a HLS y reproductor en escritorio y móvil. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android con visor de cámaras en directo (HLS/ExoPlayer), notificaciones push (FCM) al detectar eventos, lista de grabaciones con miniaturas y descarga para ver offline; permisos y trabajo en segundo plano. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mosaico de cámaras en vivo, línea de tiempo con scrub de eventos, panel de configuración, componente personalizado de reproducción y modo oscuro/accesibilidad. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Es el corazón del proyecto: hilos de captura concurrentes, pools, colas productor-consumidor con sincronización, comunicación por sockets/WebSocket con los clientes y un servicio de sistema gestionado por systemd. Se pueden demostrar condiciones de carrera y su solución. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: Odoo/Dolibarr para llevar los clientes (comunidades, empresas), contratos de mantenimiento y facturación de las instalaciones, integrado por API. |

**Por qué mola**

- Es el proyecto que más RAs cubre a la vez y de forma natural, sin 'coser' módulos.
- Demo brutal: mueves la mano delante de una cámara y suena el móvil en directo.
- El apartado de seguridad y RGPD da muchísimo juego en la memoria.

**Riesgos y cómo mitigarlos**

- Rendimiento: empieza con 2-3 cámaras y resolución baja; las cámaras pueden ser móviles con app IP o vídeos de prueba en bucle.
- Legalidad de la videovigilancia: plantéalo como maqueta con cámaras ficticias o sobre tu propia red de laboratorio.
- Alcance: recorta la visión artificial a detección de movimiento si ves que se desborda.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Captura de 2 cámaras RTSP; Grabación por eventos; Visor de escritorio en directo; App móvil con aviso push |
| Fase 2 | Línea de tiempo y búsqueda de eventos; Detección de personas; RBAC y auditoría; Retención y copias |
| Fase 3 | ONVIF (descubrimiento de cámaras); Transcodificación adaptativa; Integración ERP-CRM |

---

### 4.2 📦 LogiScan — Almacén con PDA, códigos de barras y RFID

*El RA dice literalmente 'teléfonos, PDA y otros dispositivos móviles': aquí la PDA es la protagonista.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 120-160 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | móvil, PDA, ERP-CRM, sincronización, logística |

**De qué va.** App Android para PDA/smartphone con lector de códigos de barras y RFID que cubre recepción de mercancía, ubicación, inventario rotativo y preparación de pedidos (picking), funcionando sin conexión y sincronizando después. Escritorio para jefes de almacén con mapa de ubicaciones, informes y cuadro de mando. Integración con un ERP (Odoo) para stock, compras y facturación.

**Arquitectura (de un vistazo)**

- App móvil: SQLite/Room local + cola de operaciones pendientes + sincronización con resolución de conflictos.
- Servicio de sincronización multihilo (varios PDA a la vez) con control de concurrencia sobre el stock.
- Escritorio: mapa del almacén en 2D, informes PDF/Jasper y dashboard de rotación de stock.
- Conector con Odoo vía XML-RPC/JSON-RPC para pedidos, albaranes y facturación.
- Servidor con API REST, JWT y roles (operario, supervisor, administración).

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Móvil | Android Kotlin + ML Kit (escaneo) + Room + WorkManager |
| PDA | PDA Android con pistola láser o móvil con cámara (modo lector) |
| Escritorio | JavaFX o C# WPF/WinUI según lo que domines |
| Servicio | Java Spring Boot o Node/Express con pool de hilos |
| Datos | PostgreSQL o MySQL + SQLite local en el móvil |
| ERP | Odoo Community (Docker) + API RPC |
| Infra | Servidor Linux + Docker + Nginx + copias automáticas |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor con Docker, servicio systemd, acceso por red interna, copias y restauración del ERP. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Autenticación por token, roles, trazabilidad de quién mueve cada artículo, copias cifradas y registro de auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo de almacén (ubicaciones, lotes, movimientos, auditoría de stock), integridad referencial, transacciones y procedimientos de regularización. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Automatización de builds, versionado de la API, pruebas de sincronización y despliegue en dos entornos. |
| ✔ **Acceso a datos** (`AD`) | Capa de acceso a datos en el móvil y en el servidor, mapeo ORM, consultas de stock por ubicación y lotes. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Generación de informes PDF con códigos de barras/QR, captura de fotos de incidencias en recepción y gráficos de rotación. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android completa: ciclo de vida, cámara como escáner, persistencia local, trabajo en segundo plano, notificaciones y funcionamiento offline con sincronización posterior. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mapa interactivo de ubicaciones del almacén (componente personalizado), grids de picking, validaciones y atajos de teclado para uso intensivo. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Servidor multihilo que atiende varias PDA concurrentes, más workers de sincronización y de generación de informes; locks o transacciones para no romper el stock. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Implantación real de Odoo: evaluación de módulos (Inventario, Compras, Ventas, Facturación), migración de datos desde el sistema 'antiguo' y verificación de integridad. |

**Por qué mola**

- Es el proyecto donde el RA de móviles encaja de forma literal y defendible ante el tribunal.
- La sincronización offline es un problema técnico real, con conflictos que hay que resolver: eso puntúa.
- Se puede presentar como caso real de una empresa (ficticia) y el ERP-CRM entra solo.

**Riesgos y cómo mitigarlos**

- Si no tienes PDA física, usa el móvil como lector y documéntalo como decisión de diseño.
- La resolución de conflictos offline puede comerse horas: define reglas simples (última escritura por campo + log).
- Odoo consume tiempo en instalación: levántalo en Docker el primer día y no lo toques más.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Escaneo y alta de artículos; Recepción y ubicación; Sincronización básica; CRUD de escritorio |
| Fase 2 | Inventario rotativo; Picking con lista optimizada; Informes PDF; Integración Odoo |
| Fase 3 | RFID; Cuadro de mando; Modo offline completo con resolución de conflictos |

---

### 4.3 🏋️ GymCore — ERP-CRM de gimnasio con app de socio y multimedia

*Reservas, acceso por QR, rutinas en vídeo y cuotas facturadas desde el ERP: el pack completo.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 130-170 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | ERP-CRM, móvil, multimedia, gráficas, negocio |

**De qué va.** Sistema integral para un gimnasio: app móvil del socio (reserva de clases, QR de acceso, rutinas con vídeos y seguimiento de progreso), aplicación de escritorio para recepción y entrenadores (altas, control de accesos en tiempo real, cuadro de mando) y un servicio multihilo que sincroniza presencia y notificaciones. La facturación recurrente, la captación y la fidelización viven en el ERP-CRM.

**Arquitectura (de un vistazo)**

- Servicio multihilo: control de accesos en tiempo real (entradas por QR), temporizadores de reservas y notificaciones.
- App Android del socio: Room offline, notificaciones push, reproductor de vídeo de ejercicios, gráficos de progreso.
- Escritorio: panel por roles (recepción, entrenador, gerencia), calendario de clases y gráficas de ocupación.
- Odoo/Dolibarr: cuotas recurrentes, CRM de captación, facturación y contabilidad.
- API REST central con JWT y RBAC; informes PDF (recibos, certificados).

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Escritorio | JavaFX + SceneBuilder o Electron/Tauri |
| Móvil | Kotlin Android + ExoPlayer + FCM + Room |
| Servicio | Spring Boot (hilos, scheduler, WebSockets) |
| Datos | MySQL/PostgreSQL |
| ERP | Odoo Community (Ventas, Facturación, CRM, Punto de venta) |
| Infra | Ubuntu Server + Docker + Nginx + certificados |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, contenedores, copias, servicios programados y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | JWT, 2FA para personal, RGPD de datos de salud (peso, lesiones), cifrado y auditoría de accesos. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo socios-clases-reservas-accesos con integridad referencial, transacciones y procedimientos de facturación. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI/CD, versionado, entornos separados, pruebas automatizadas y empaquetado de los tres clientes. |
| ✔ **Acceso a datos** (`AD`) | ORM con JPA/MyBatis, consultas de ocupación y reservas, consumo de la API del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Reproductor de vídeos de ejercicios, miniaturas, animaciones de progreso y generación de PDFs (recibos, informes de progreso). |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App del socio con cámara (QR), notificaciones, almacenamiento local y sincronización de reservas. |
| ✔ **Desarrollo de interfaces** (`DI`) | Paneles por rol, calendario drag&drop, componentes de gráficas personalizados y validación de formularios. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Servicio concurrente de accesos, scheduler de caducidad de reservas y notificaciones, y workers de facturación mensual. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | El más fuerte de la lista en ERP-CRM: implantación de Odoo, evaluación de módulos (Ventas, Suscripciones, CRM, Contabilidad), migración de socios y verificación de integridad de los datos. |

**Por qué mola**

- Contexto de negocio realista y fácil de explicar; el tribunal lo entiende en 30 segundos.
- Todo el mundo ha pisado un gimnasio: es facilísimo encontrar 'cliente' (el del barrio) para el análisis de requisitos.
- El ERP-CRM encaja sin forzarlo (cuotas, CRM, facturación recurrente).

**Riesgos y cómo mitigarlos**

- Alcance enorme: elige 2 de 3 frentes (por ejemplo móvil + escritorio + ERP, y deja fuera la nutrición).
- Datos de salud → RGPD: usa datos ficticios y explica las medidas en la memoria (más puntos).
- Evita duplicar lo que ya hace Odoo: tu app hace lo que el ERP no hace.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Socios y clases; Reservas desde el móvil; Acceso por QR; Cuotas en Odoo |
| Fase 2 | Rutinas con vídeo; Gráficas de progreso; Notificaciones; Dashboard de ocupación |
| Fase 3 | CRM de captación con embudo; Tienda/punto de venta; App del entrenador |

---

### 4.4 🛡️ NetSentinel — Monitorización de red y mini-SOC

*Descubre los equipos de la red, vigílalos a la vez y recibe la alerta antes de que caiga el servicio.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 110-150 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | redes, seguridad, multihilo, sistemas |

**De qué va.** Servicio multiproceso que sondea en paralelo decenas de equipos (ICMP, SNMP, puertos y servicios), detecta caídas, nuevos dispositivos no autorizados y anomalías, y genera alertas. Panel de escritorio con mapa de red en vivo, gráficas de disponibilidad y línea de tiempo de incidencias; app Android que recibe las alertas y permite reconocerlas (ack) y consultar el estado.

**Arquitectura (de un vistazo)**

- Motor de sondeo multihilo con pool configurable y planificador de tareas periódicas.
- Proceso recolector de métricas + proceso de correlación/reglas de alerta.
- Almacenamiento de series temporales y eventos con retención configurable.
- Escritorio: mapa de red, gráficas, reglas y generación de informes PDF.
- Móvil: alertas push, lista de incidencias y acciones rápidas.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Servicio | Python (asyncio/concurrent.futures + SNMP) o Java (hilos + snmp4j) |
| Escritorio | JavaFX o Python + Qt/PySide |
| Móvil | Kotlin Android + FCM |
| Datos | PostgreSQL (+ TimescaleDB si te atreves) o InfluxDB |
| Infra | Servidor Linux + Docker + red de laboratorio con máquinas virtuales |
| Gráficas | JFreeChart / Charts de Android / ECharts embebido |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | El proyecto más fuerte en configuración y explotación: servidor Linux, servicios, SNMP, DNS/DHCP, red de laboratorio con VMs, copias y monitorización del propio monitor. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Seguridad por todas partes: detección de dispositivos no autorizados, escaneo de puertos, endurecimiento del servidor, TLS, RBAC, auditoría, gestión de secretos y plan de seguridad documentado. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo de dispositivos/métricas/alertas, retención, integridad y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Automatización de despliegue, pruebas de carga del sondeo y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | Acceso a datos de métricas y eventos, consultas agregadas y exportación. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Iconografía y gráficos de estado, generación de informes PDF y sonidos/alarmas. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de alertas con notificaciones push y acciones rápidas. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mapa de red interactivo (componente personalizado con nodos y aristas), gráficas de disponibilidad y filtros. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Pool de hilos de sondeo, proceso separado de correlación, comunicación por sockets y planificación concurrente: puro PSP. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: gestión de incidencias y SLA en el ERP-CRM (partes de trabajo y facturación de horas). |

**Por qué mola**

- Cubre los dos RAs de Sistemas Informáticos con soltura, que suelen ser los más difíciles de justificar.
- Es muy vistoso en la defensa: desenchufas un cable de red y salta la alerta en el móvil.
- Se monta enteramente con máquinas virtuales, así que no necesitas hardware.

**Riesgos y cómo mitigarlos**

- El laboratorio de red puede dar guerra: monta primero 2-3 VMs y úsalas como 'la red de la empresa ficticia'.
- Cuidado con montar un escáner y usarlo fuera de tu red de laboratorio: acótalo por diseño y documéntalo.
- Riesgo de 'clon de Nagios': diferénciate con el móvil, las reglas y el mapa en vivo.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Sondeo concurrente de equipos; Detección de caídas; Panel con lista y gráficas; Alertas push |
| Fase 2 | Mapa de red; Reglas de alerta personalizables; Histórico e informes; Detección de intrusos |
| Fase 3 | SNMP avanzado; Autodescubrimiento; Integración ERP-CRM de partes de trabajo |

---

### 4.5 🍿 StreamHub — Servidor multimedia y streaming (estilo Plex propio)

*Transcodifica bajo demanda, lleva el catálogo en la BD y sigue viendo la peli en el móvil donde la dejaste.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 120-160 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | multimedia, multihilo, móvil, streaming |

**De qué va.** Servidor que cataloga una biblioteca de vídeo y audio, extrae metadatos y carátulas, transcodifica bajo demanda según el dispositivo y sirve streaming adaptativo (HLS). Cliente de escritorio de gestión y reproducción, y app Android con reproductor, reanudación entre dispositivos y descargas para ver sin conexión. Perfiles de usuario, control parental y control de acceso.

**Arquitectura (de un vistazo)**

- Servicio de transcodificación: cola de trabajos FFmpeg con workers concurrentes y caché.
- Servidor HTTP/WebSocket para streaming HLS y sincronización de progreso.
- Catálogo en BD con metadatos, carátulas, subtítulos y perfiles.
- Escritorio: gestión de biblioteca, reproducción y estadísticas de visionado.
- Móvil: ExoPlayer, descargas offline, casting y control parental.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Servicio | Java (Spring Boot) o Python (FastAPI) + FFmpeg |
| Escritorio | JavaFX + VLC embebido (vlcj) o Tauri |
| Móvil | Kotlin + ExoPlayer + Room |
| Datos | PostgreSQL + almacenamiento de ficheros + caché de transcodificación |
| Infra | Debian + Docker + Nginx + TLS |
| Metadatos | API pública o ficheros NFO locales |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, systemd, almacenamiento, contenedores, copias y monitorización del servicio. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Autenticación, perfiles y control parental, TLS, tokens de streaming temporales y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo de biblioteca (obras, episodios, metadatos, perfiles, historial), integridad y copias de metadatos. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Automatización de builds, pruebas de transcodificación y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | Persistencia del catálogo, índices de búsqueda y sincronización del progreso de reproducción. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | El rey del multimedia: vídeo, audio, códecs, transcodificación, miniaturas, subtítulos, streaming y reproducción multiplataforma. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android con reproducción, descargas y notificaciones de nuevos episodios. |
| ✔ **Desarrollo de interfaces** (`DI`) | Galería de carátulas, reproductor con controles personalizados, perfiles y panel de administración. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Cola de transcodificación multihilo/proceso, límite de workers, cancelación de trabajos y streaming concurrente a varios clientes. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: ERP-CRM para socios/suscripciones y facturación de planes premium. |

**Por qué mola**

- Multimedia y multihilo son los dos RAs más 'divertidos' y aquí son el núcleo, no un añadido.
- Demo perfecta: empiezas en el portátil y sigues en el móvil por donde ibas.
- Escalable en horas: con 3 pelis de dominio público tienes biblioteca de prueba.

**Riesgos y cómo mitigarlos**

- Derechos de autor: usa contenido propio, de dominio público o Creative Commons y documéntalo.
- Transcodificar es caro en CPU: limita resoluciones y usa caché; graba vídeos cortos de prueba.
- Riesgo de parecer 'un clon de Plex': apórtale el control parental, el progreso cross-device y el panel de administración.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Catálogo y metadatos; Reproducción web/escritorio; Transcodificación en un worker; App móvil básica |
| Fase 2 | Streaming HLS adaptativo; Varios workers concurrentes; Descarga offline; Reanudación cross-device |
| Fase 3 | Control parental avanzado; Subtítulos automáticos; Estadísticas y recomendaciones |

---

### 4.6 🚚 FleetTrack — Flota y reparto con seguimiento GPS en vivo

*Ves los vehículos moverse en el mapa y la prueba de entrega llega con foto, firma y coordenadas.*

| | |
|---|---|
| Dificultad | ●●●●● (5/5) |
| Esfuerzo estimado | 140-180 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | móvil, GPS, mapas, sockets, ERP-CRM |

**De qué va.** App Android del conductor con hoja de ruta, navegación y prueba de entrega (foto, firma y GPS). Servidor multihilo que ingesta posiciones por sockets/WebSocket, calcula geocercas y genera alertas. Panel de escritorio con mapa en vivo de la flota, optimización de rutas y cuadro de mando; los albaranes y la facturación se cierran en el ERP-CRM.

**Arquitectura (de un vistazo)**

- App de conductor: servicio en primer plano de localización, cola de envíos offline y sincronización por lotes.
- Servidor de ingesta multihilo (Netty/sockets o WebSocket) con cálculo de geocercas en workers.
- Panel de escritorio: mapa en vivo (Leaflet/Google Maps embebido), asignación de rutas y KPIs.
- ERP: albaranes, partes y facturación en Odoo vía API.
- Almacenamiento espacial (PostGIS) y series de posiciones.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Móvil | Kotlin + Fused Location + Room + WorkManager + cámara |
| Servidor | Java Netty/Spring WebFlux o Node + WebSocket |
| Escritorio | JavaFX con WebView (Leaflet) o Electron |
| Datos | PostgreSQL + PostGIS |
| ERP | Odoo (Ventas, Inventario, Facturación) |
| Infra | Linux + Docker + Nginx + TLS |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, contenedores, servicios, monitorización y copias. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Tokens JWT, TLS, control de permisos por conductor, privacidad de la geolocalización (RGPD) y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo con datos espaciales, integridad de albaranes/entregas, transacciones y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, entornos, pruebas de carga de ingesta GPS y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | Persistencia de posiciones, rutas y entregas; consultas espaciales; cliente de la API del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Captura y tratamiento de fotos de entrega, firma como imagen, generación de albaranes PDF y gráficos de KPIs. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de campo de libro: localización en segundo plano, cámara, firma táctil, modo offline y sincronización. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mapa en vivo con marcadores y rutas (componente personalizado o WebView integrado), panel de despacho. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Servidor de sockets concurrente con miles de posiciones, workers de geocercas y procesos de cálculo de rutas. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Implantación de Odoo para clientes, albaranes y facturación; evaluación de módulos e integridad tras la migración. |

**Por qué mola**

- El mapa en vivo es de lo más impactante que puedes enseñar en una defensa.
- Caso de uso real y fácil de vender: 'empresa de reparto local'.
- Combina móvil + PSP + mapas + ERP sin parecer artificial.

**Riesgos y cómo mitigarlos**

- No necesitas vehículos reales: simula recorridos con ficheros GPX o un script que mueva marcadores.
- El seguimiento GPS continuo gasta batería: documéntalo como decisión de diseño (frecuencia adaptativa).
- PostGIS añade complejidad; si te atasca, usa lat/long con índices normales.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | App conductor con ruta; Envío de posiciones; Mapa en vivo en escritorio; Entrega con foto+firma |
| Fase 2 | Geocercas y alertas; Modo offline; KPIs y rutas; PDF de albarán |
| Fase 3 | Optimización de rutas; Integración ERP-CRM; Simulador GPX para demos |

---

### 4.7 🎫 HelpDesk Pro — Gestión de incidencias con SLA y app de técnico

*Tickets con SLA, técnicos en campo y facturación de horas: el clásico, pero bien hecho.*

| | |
|---|---|
| Dificultad | ●●●○○ (3/5) |
| Esfuerzo estimado | 100-140 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | escritorio, móvil, SLA, ERP-CRM, seguro |

**De qué va.** Sistema de tickets con categorías, prioridades y SLA con temporizadores reales, asignación automática, chat multihilo entre cliente y técnico, adjuntos multimedia (capturas y screencasts) y base de conocimientos. App Android para técnicos en campo con partes de trabajo, fotos, firma del cliente y geolocalización. Las horas y los contratos de soporte se facturan desde el ERP-CRM.

**Arquitectura (de un vistazo)**

- Servicio con scheduler de SLA y workers de notificaciones (correo + push).
- Chat interno con WebSockets y salas por ticket.
- Escritorio: bandeja de tickets, tablero Kanban, dashboard de cumplimiento de SLA.
- Móvil: partes de trabajo offline, firma y fotos.
- ERP: partes de horas, contratos, facturación y CRM.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Escritorio | JavaFX o web (Spring Boot + Thymeleaf/React embebido) |
| Móvil | Kotlin Android + Room + FCM |
| Servicio | Spring Boot (hilos, scheduler, WebSocket) |
| Datos | MySQL/PostgreSQL |
| ERP | Odoo/Dolibarr (Proyectos, Facturación, CRM) |
| Infra | Linux + Docker + Nginx |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, servicios, copias y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Roles (cliente/técnico/admin), 2FA, auditoría de quién cambia cada ticket y copias seguras. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo de tickets/estados/histórico, integridad, transacciones y auditoría de cambios. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI/CD, pruebas de API, entornos y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas complejas de tickets, integración con la API del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Adjuntos con capturas, screencasts y generación de PDFs de partes de trabajo. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de técnico con trabajo offline, cámara, firma y GPS. |
| ✔ **Desarrollo de interfaces** (`DI`) | Interfaz rica: Kanban drag&drop, bandeja con filtros, dashboard de SLA y formularios validados. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Scheduler de SLA, workers de notificaciones, chat multihilo y procesos de generación de informes. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Implantación del ERP para contratos de soporte, partes de horas y facturación. |

**Por qué mola**

- El más seguro: alcance controlable y todos los módulos tienen un hueco evidente.
- El SLA es un requisito real que te obliga a usar hilos/temporizadores de verdad.
- Fácil de explicar y de ampliar si te sobra tiempo.

**Riesgos y cómo mitigarlos**

- Es el menos original: diferénciate con el móvil, el SLA y la integración ERP.
- Sin una demo de datos decente parece vacío: prepara un generador de datos de prueba.
- Cuidado con no reinventar el ERP: delimita qué vive en tu app y qué en Odoo.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Tickets y estados; Asignación; Dashboard; Roles y login |
| Fase 2 | SLA y temporizadores; Chat multihilo; Adjuntos multimedia; App de técnico |
| Fase 3 | Base de conocimientos; Facturación en ERP; Informes avanzados |

---

### 4.8 📄 DocuFlow — Digitalización certificada y gestor documental con OCR

*Escaneas, el OCR indexa solo y cada documento queda trazado, cifrado y firmado.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 120-160 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | imagen, OCR, colas, seguridad, ERP-CRM |

**De qué va.** Pipeline multiproceso que convierte papel en documentos indexados: escaneo o foto desde el móvil, mejora y recorte automático de imagen, OCR, clasificación y publicación en un repositorio con búsqueda a texto completo. Visor de escritorio con anotaciones y control de versiones, flujo de aprobación y trazabilidad; cifrado, sellado temporal con hash y auditoría de accesos; integración con el ERP para expedientes de clientes.

**Arquitectura (de un vistazo)**

- Cola de trabajos: workers concurrentes de mejora de imagen, OCR en proceso separado e indexación.
- Almacén de documentos cifrado + índice de búsqueda (Postgres FTS o Elasticsearch/OpenSearch).
- Escritorio: visor, anotaciones, metadatos, flujo de aprobación y auditoría.
- Móvil: captura con detección de bordes y subida en segundo plano.
- ERP: expedientes de cliente, presupuestos y facturación asociados al documento.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Procesamiento | Python (OpenCV, Tesseract, Pillow) + Celery o Java con procesos externos |
| Escritorio | JavaFX o Electron/Tauri |
| Móvil | Kotlin + CameraX + OpenCV Android |
| Datos | PostgreSQL (FTS) + almacenamiento cifrado |
| ERP | Odoo/Dolibarr (documentos y facturación) |
| Infra | Linux + Docker + Nginx + copias cifradas |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, contenedores, almacenamiento, copias y servicios. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Cifrado en reposo, control de acceso granular, sellado con hash, registro de auditoría inmutable y RGPD (plazos de conservación). |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo documental (expedientes, versiones, permisos, log), integridad referencial y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Automatización, pruebas sobre el pipeline y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | Persistencia de documentos, metadatos y versiones; indexación y búsqueda. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Tratamiento de imagen (recorte, binarización, deskew), OCR, miniaturas y generación de PDFs. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de captura con procesamiento de imagen y subida diferida. |
| ✔ **Desarrollo de interfaces** (`DI`) | Visor con zoom y anotaciones, árbol de expedientes, búsqueda avanzada y flujo de aprobación visual. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Pipeline multiproceso con colas, workers, reintentos y cancelación: caso de manual de PSP. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Expedientes y facturación en el ERP, con verificación de integridad de los datos migrados. |

**Por qué mola**

- Tiene un problema técnico real y medible: calidad del OCR, concurrencia de la cola.
- El apartado de seguridad y cumplimiento es de los más sólidos que puedes presentar.
- Se prueba con documentos que puedes generar tú mismo: cero contenido con derechos de autor.

**Riesgos y cómo mitigarlos**

- El OCR en español necesita diccionarios y buen preprocesado: prueba primero con PDFs escaneados nítidos.
- Elasticsearch pesa en RAM: empieza con la búsqueda de texto completo de Postgres.
- Define un corpus de prueba pequeño y reproducible para medir aciertos del OCR.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Subida y mejora de imagen; OCR en workers; Búsqueda; Visor de escritorio |
| Fase 2 | Versiones y aprobaciones; Captura móvil; Permisos granulares y auditoría; PDFs |
| Fase 3 | Clasificación automática; Sellado temporal; Integración ERP-CRM |

---

### 4.9 🏠 EcoDomus — Domótica y control de accesos con Raspberry Pi

*Luces, sensores, cerradura y cámara: todo orquestado por hilos y controlado desde el móvil.*

| | |
|---|---|
| Dificultad | ●●●●● (5/5) |
| Esfuerzo estimado | 140-180 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | IoT, hardware, móvil, seguridad, tiempo real |

**De qué va.** Hub en Raspberry Pi que lee sensores y controla actuadores por MQTT, gestiona una cerradura con RFID/NFC y una cámara, y ejecuta reglas de automatización. Panel de escritorio con planos interactivos de la vivienda y gráficas de consumo en tiempo real, y app Android para control remoto, apertura de puerta y alertas, con la red IoT aislada y endurecida.

**Arquitectura (de un vistazo)**

- Hub: hilos por bus de sensores, cliente MQTT y motor de reglas con prioridades.
- Servicio de cámaras (streaming y detección) y servicio de control de accesos con registro de eventos.
- Broker MQTT (Mosquitto) con TLS y autenticación por cliente.
- Escritorio: plano interactivo, gráficas en vivo y editor de reglas.
- Móvil: control, notificaciones y apertura remota con 2FA.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Hub | Raspberry Pi OS + Python (hilos/MQTT) o Java |
| Hardware | RPi 4, sensores (DHT22, PIR), relés, ESP32, lector RFID, cerradura eléctrica, cámara |
| Broker | Mosquitto con TLS |
| Escritorio | JavaFX o Python + Qt |
| Móvil | Kotlin + MQTT/FCM |
| Datos | PostgreSQL o SQLite + series temporales |
| Infra | VLAN para IoT + WireGuard para acceso remoto |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Configuración del SO en la RPi, servicios, red (VLAN IoT, DNS local), copias de la configuración y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Red aislada, MQTT con TLS y certificados de cliente, 2FA para apertura, registro de accesos y endurecimiento del dispositivo. |
| ✔ **Gestión de bases de datos** (`BD`) | Series temporales, retención y agregados; integridad y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Despliegue automatizado en la RPi, pruebas sobre el motor de reglas y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | Persistencia de lecturas, eventos y reglas; consultas de históricos. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Streaming de cámara, captura de imágenes y gráficos/animaciones del estado de la casa. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de control con notificaciones push y acción remota sobre el hub. |
| ✔ **Desarrollo de interfaces** (`DI`) | Plano interactivo de la vivienda (componente personalizado), gráficas en vivo y editor visual de reglas. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Hilos concurrentes por sensor/actuador, motor de reglas con sincronización, colas de eventos y servicios del sistema. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: ERP-CRM para instaladores, presupuestos y mantenimiento de instalaciones. |

**Por qué mola**

- Es el más 'chulo' si te van el hardware y las redes: enchufar y que pase algo.
- Seguridad y sistemas se justifican solos (IoT es un desastre de seguridad y tú lo arreglas).
- Las gráficas en tiempo real en el panel quedan espectaculares.

**Riesgos y cómo mitigarlos**

- Dependes del hardware: ten un plan B con sensores simulados por software documentado.
- La RPi puede quedarse corta con vídeo: baja resolución o separa la cámara en otro dispositivo.
- El cableado/electrónica come horas: compra módulos ya montados (relés, sensores con carcasa).

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | 2-3 sensores + 2 actuadores; Broker MQTT con TLS; Panel con estado y gráficas; App de control |
| Fase 2 | Reglas y automatizaciones; Cerradura RFID con registro; Cámara y streaming; Notificaciones |
| Fase 3 | Consumo energético e informes; Apertura remota con 2FA; Integración ERP-CRM de instalaciones |

---

### 4.10 🍽️ MesaFácil — Reservas para restaurante o alojamiento rural

*Concurrencia de verdad: dos clientes, la última mesa, una sola reserva.*

| | |
|---|---|
| Dificultad | ●●●○○ (3/5) |
| Esfuerzo estimado | 100-140 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | concurrencia, BD, móvil, pagos, ERP-CRM |

**De qué va.** Motor de reservas con control estricto de solapamientos, bloqueo optimista/pesimista y transacciones, app móvil del cliente (reservar, modificar, check-in con QR, notificaciones y galería multimedia) y panel de escritorio con calendario drag&drop, mapa de mesas o habitaciones y gráficas de ocupación. Pagos de señal en sandbox y facturación en el ERP-CRM.

**Arquitectura (de un vistazo)**

- API REST con transacciones y control de concurrencia sobre disponibilidad.
- Servicio de notificaciones (correo + push) y recordatorios programados (hilos/tareas).
- Escritorio: calendario, mapa de mesas/habitaciones, ocupación y previsiones.
- Móvil: reservas, código QR, galería de fotos y valoraciones.
- ERP: facturación, clientes y fidelización.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Escritorio | JavaFX o C# WPF |
| Móvil | Kotlin Android + FCM + Room |
| Servicio | Spring Boot o Node/Express |
| Datos | PostgreSQL/MySQL con transacciones y bloqueo optimista |
| Pagos | Stripe/Redsys en modo sandbox (nunca real) |
| ERP | Odoo/Dolibarr (Ventas, Facturación, CRM) |
| Infra | Linux + Docker + Nginx |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, contenedores, copias y servicios. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Autenticación, RGPD de datos de clientes, pagos en sandbox con tokenización y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | El más fuerte en bases de datos: integridad de la disponibilidad, transacciones, bloqueos, procedimientos y pruebas de concurrencia. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, pruebas de concurrencia automatizadas, entornos y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM con control de versiones (bloqueo optimista), consultas de disponibilidad y cliente del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Galería de imágenes del establecimiento, generación de PDFs de confirmación y gráficas. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App de cliente con QR, notificaciones y galería multimedia. |
| ✔ **Desarrollo de interfaces** (`DI`) | Calendario drag&drop, mapa de mesas/habitaciones con estados por color y panel de ocupación. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Pruebas de carga concurrentes sobre el motor de reservas, workers de notificaciones y tareas programadas. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | ERP para facturación, CRM y fidelización; migración de clientes y verificación de integridad. |

**Por qué mola**

- Es el más asequible: el alcance se recorta fácil y siempre queda algo presentable.
- El problema de concurrencia es perfecto para lucirte en BD y PSP a la vez.
- Proyecto ideal si quieres 'algo terminado' y no una demo a medias.

**Riesgos y cómo mitigarlos**

- Pagos: usa siempre sandbox y documenta que no se procesan pagos reales.
- Es el menos espectacular visualmente: compénsalo con un buen panel y gráficas.
- Prepara un simulador de carga (N hilos intentando reservar la misma mesa) para la defensa.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Disponibilidad y reservas; Panel de escritorio; App de cliente; Notificaciones |
| Fase 2 | Pagos de señal en sandbox; Check-in QR; Ocupación y previsiones; Integración ERP |
| Fase 3 | Lista de espera automática; Valoraciones y multimedia; App de camareros |

---

## 5. Ideas rápidas (plan B)

Proyectos más pequeños por si tu centro te limita el alcance o vas justo de tiempo.

| Idea | Qué aporta | Bloques que cubre |
|------|------------|-------------------|
| **Préstamo de equipos del centro (aulas/material)** | App móvil con escaneo de códigos de barras, escritorio para el conserje y control de incidencias. Pequeño, cerrado y 100% terminable. | `PMDM·MOV`, `AD`, `DI`, `BD` |
| **Clon de Spotify para el catálogo de audio del ciclo** | Podcasts y audios propios, streaming multihilo, app móvil con reproducción offline y panel de subida. | `PMDM·M`, `PSP`, `PMDM·MOV`, `DI` |
| **Generador automático de horarios escolares** | Algoritmo con restricciones ejecutado en varios hilos, interfaz para fijar restricciones y exportación a PDF/Excel. | `PSP`, `DI`, `PMDM·M`, `BD` |
| **Sistema de control de presencia con reconocimiento facial** | Captura con OpenCV, comparación de embeddings, panel de escritorio y justificantes. Ojo con RGPD: datos sintéticos. | `PMDM·M`, `SI-RA6`, `PSP`, `DI` |
| **Simulador de bolsa con datos en tiempo real** | Ingesta multihilo de datos de mercado, gráficas en vivo, carteras y alertas móviles. Sin dinero real. | `PSP`, `DI`, `PMDM·MOV`, `AD` |
| **Plataforma de tutorías y seguimiento académico** | Citas, chat multihilo, informes PDF con gráficas y app móvil con recordatorios. Encaja bien con un centro educativo real. | `DI`, `PSP`, `PMDM·MOV`, `PMDM·M` |

## 6. Recomendación según tu perfil

**→ Si quieres el proyecto más completo y 'molón': SentinelVIS — Tu propio NVR de videovigilancia IP**

Cubre prácticamente todos los RAs de forma natural y la demo es de las más impactantes: mueves la mano ante la cámara y salta la alerta en el móvil. A cambio, es el de mayor riesgo técnico: acota a 2-3 cámaras y deja la visión artificial para la fase 2.

**→ Si quieres ir sobre seguro y tenerlo terminado: MesaFácil — Reservas para restaurante o alojamiento rural**

Alcance pequeño, problema técnico real (concurrencia) y todos los módulos tienen hueco. Es el que menos probabilidades tiene de quedarse a medias.

**→ Si el ERP-CRM te da respeto: LogiScan — Almacén con PDA, códigos de barras y RFID**

El almacén necesita el ERP de verdad (stock, compras, facturación), así que el RA entra por necesidad y no por adorno. Además, la PDA justifica el RA de móviles tal cual está redactado.

**→ Si te mola el hardware y las redes: EcoDomus — Domótica y control de accesos con Raspberry Pi**

Es el más espectacular y el que mejor justifica seguridad y sistemas. Solo si tienes la Raspberry y tiempo para pelearte con sensores; si no, pasa a NetSentinel que se monta con VMs.

**→ Si el tribunal valora mucho la defensa: GymCore — ERP-CRM de gimnasio con app de socio y multimedia**

Contexto de negocio que cualquiera entiende en 30 segundos y que te permite lucirte explicando decisiones. Menos riesgo técnico, más storytelling.

## 7. Checklist de elección

Antes de cerrar la idea, responde honestamente:

1. ¿Cubre al menos 6-7 de los 9 bloques de RAs sin inventarte funcionalidades que nadie pediría?
2. ¿Tienes una demo que se vea en 2 minutos y que falle poco el día de la defensa?
3. ¿Puedes recortar el 30% del alcance y que siga teniendo sentido? (si no, el alcance es excesivo)
4. ¿El ERP-CRM tiene encaje real o lo estás metiendo con calzador? (si es con calzador, el tribunal lo nota)
5. ¿Hay un problema técnico 'duro' (concurrencia, multimedia, tiempo real) que luzcas en PSP o PMDM?
6. ¿Puedes generar datos de prueba creíbles sin depender de terceros?
7. ¿Te apetece de verdad? Vas a echarle muchas horas.

## 8. Estructura propuesta de la memoria

1. Introducción: contexto, problema, motivación y por qué este proyecto (aquí vendes el 'chulo').
2. Análisis: estudio de alternativas existentes, requisitos funcionales y no funcionales, casos de uso, actores, prototipos de interfaz.
3. Diseño: arquitectura (diagrama de componentes y despliegue), modelo de datos (ER y relacional), diseño de interfaces, protocolos, seguridad y plan de seguridad.
4. Planificación y presupuesto: estimación, diagrama de Gantt, costes de hardware, software y horas (EIE).
5. Implementación y verificación: entornos de desarrollo, control de versiones, pruebas (unitarias, integración, carga, usabilidad) y resultados.
6. Implantación: manual de instalación, configuración del servidor, copias de seguridad y plan de seguridad aplicado.
7. Conclusiones y líneas futuras.
8. Anexos: manual de usuario (escritorio y móvil), manual de administración/instalación, código fuente (enlace al repositorio), diccionario de datos, guion de la demo y capturas.

## 9. Trampas clásicas

- Un CRUD con login: no llega, por mucho que le pongas gráficas.
- Depender de una API externa que puede caerse o cambiar el día de la defensa: ten siempre datos en local.
- Meter el ERP porque 'hay que meterlo': si no hay migración de datos ni evaluación de módulos, no cuenta como RA.
- La app móvil de relleno: que tenga sentido offline y use algo del dispositivo (cámara, GPS, sensores, notificaciones).
- Empezar por la interfaz y dejar la infraestructura (SI/seguridad) para el final: el despliegue documentado es medio proyecto.
- No versionar desde el día 1: el historial de Git es una prueba más del trabajo.

---

¿Quieres que desarrolle una de estas ideas en profundidad (análisis de requisitos, modelo de datos, 
arquitectura y planificación)? Dime cuál y la convierto en el documento base del proyecto.
