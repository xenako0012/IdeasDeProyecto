# Banco de ideas para el Proyecto Intermodular

**Técnico Superior en Desarrollo de Aplicaciones Multiplataforma (DAM) · 2º curso · última actualización: 2026-11-09**

> Los Resultados de Aprendizaje (RA) listados en 'modulos' son los que has aportado; el código de módulo es el del currículo LOE de DAM (RD 1584/2011), confírmalo con tu centro por si hay adaptación autonómica.

## Cómo usar este documento

1. Lee primero la **[guía para juegos en el navegador](#4-juegos-en-el-navegador)**: las reglas del juego aquí son distintas.
2. Compara con la **[matriz de cobertura](#3-matriz-de-cobertura)** qué idea toca cuántos módulos.
3. Lee solo las fichas de las 3-4 ideas que te encajen.
4. Pásales el **[checklist de elección](#8-checklist-de-elección)** antes de decidirte.
5. Si necesitas algo más pequeño, mira las **[ideas rápidas](#7-ideas-rápidas-plan-b)**.

Tabla de contenidos:

1. [RA → módulo: qué te van a pedir](#1-ra--módulo-qué-te-van-a-pedir)
2. [Resumen de ideas](#2-resumen-de-ideas)
3. [Matriz de cobertura](#3-matriz-de-cobertura)
4. [Juegos en el navegador](#4-juegos-en-el-navegador)
5. [Otras ideas (por si cambias de rumbo)](#5-otras-ideas-por-si-cambias-de-rumbo)
6. [Recomendación según tu perfil](#6-recomendación-según-tu-perfil)
7. [Ideas rápidas (plan B)](#7-ideas-rápidas-plan-b)
8. [Checklist de elección](#8-checklist-de-elección)
9. [Estructura propuesta de la memoria](#9-estructura-propuesta-de-la-memoria)
10. [Trampas clásicas](#10-trampas-clásicas)

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

| Tipo | Idea | Qué es | Dificultad | Esfuerzo | Bloques |
|:----:|------|--------|:----------:|:--------:|:-------:|
| 🎮 | **RiftDeck — Juego de cartas coleccionable online (TCG)** | Construyes tu mazo, juegas por turnos contra otro jugador y el servidor hace de árbitro. | ●●●●○ (4/5) | 130-170 h | 10/10 |
| 🎮 | **QuizArena — Concurso multijugador en directo** | El presentador lanza la pregunta, veinte móviles responden a la vez y el marcador sube en vivo. | ●●●○○ (3/5) | 100-140 h | 10/10 |
| 🎮 | **CodeQuest — Retos de lógica gamificados (y ejecutor en sandbox)** | Resuelves retos en el navegador, subes de nivel y compites con tu clase. | ●●●○○ (3/5) | 110-150 h | 10/10 |
| 🎮 | **HexArena — Estrategia por turnos con IA que piensa en paralelo** | Un juego de estrategia donde la IA calcula en varios hilos a la vez y puedes medir cuánto gana. | ●●●●○ (4/5) | 120-160 h | 9/10 |
| 🎮 | **Escape360 — Escape room cooperativo en 3D en el navegador** | Varias personas dentro de la misma habitación 3D, moviéndose a la vez y resolviendo puzles en equipo. | ●●●●● (5/5) | 140-180 h | 10/10 |
| 🎮 | **AutoClash — Auto-battler por rondas con simulación en el servidor** | Compras unidades y colocas el tablero; el combate lo simula el servidor en paralelo y lo ves como replay. | ●●●●○ (4/5) | 120-160 h | 10/10 |
| 🎮 | **PixelRaid — Arcade cooperativo en tiempo real (servidor autoritativo)** | Disparas en el navegador y el servidor decide si has acertado: netcode de verdad. | ●●●●● (5/5) | 150-190 h | 9/10 |
| 🎮 | **GeoSprint — Captura territorial por GPS (móvil + mapa web en vivo)** | El juego vive en tu bolsillo; el navegador es el mapa que se pinta en directo. | ●●●●○ (4/5) | 130-170 h | 10/10 |
| 💼 | **SentinelVIS — Tu propio NVR de videovigilancia IP** | Un servidor multihilo que vigila N cámaras a la vez, entiende lo que ve y te avisa al móvil. | ●●●●● (5/5) | 140-180 h | 9/10 |
| 💼 | **LogiScan — Almacén con PDA, códigos de barras y RFID** | El RA dice literalmente 'teléfonos, PDA y otros dispositivos móviles': aquí la PDA es la protagonista. | ●●●●○ (4/5) | 120-160 h | 10/10 |
| 💼 | **GymCore — ERP-CRM de gimnasio con app de socio y multimedia** | Reservas, acceso por QR, rutinas en vídeo y cuotas facturadas desde el ERP: el pack completo. | ●●●●○ (4/5) | 130-170 h | 10/10 |
| 💼 | **NetSentinel — Monitorización de red y mini-SOC** | Descubre los equipos de la red, vigílalos a la vez y recibe la alerta antes de que caiga el servicio. | ●●●●○ (4/5) | 110-150 h | 9/10 |
| 💼 | **StreamHub — Servidor multimedia y streaming (estilo Plex propio)** | Transcodifica bajo demanda, lleva el catálogo en la BD y sigue viendo la peli en el móvil donde la dejaste. | ●●●●○ (4/5) | 120-160 h | 9/10 |
| 💼 | **FleetTrack — Flota y reparto con seguimiento GPS en vivo** | Ves los vehículos moverse en el mapa y la prueba de entrega llega con foto, firma y coordenadas. | ●●●●● (5/5) | 140-180 h | 10/10 |
| 💼 | **HelpDesk Pro — Gestión de incidencias con SLA y app de técnico** | Tickets con SLA, técnicos en campo y facturación de horas: el clásico, pero bien hecho. | ●●●○○ (3/5) | 100-140 h | 10/10 |
| 💼 | **DocuFlow — Digitalización certificada y gestor documental con OCR** | Escaneas, el OCR indexa solo y cada documento queda trazado, cifrado y firmado. | ●●●●○ (4/5) | 120-160 h | 10/10 |
| 💼 | **EcoDomus — Domótica y control de accesos con Raspberry Pi** | Luces, sensores, cerradura y cámara: todo orquestado por hilos y controlado desde el móvil. | ●●●●● (5/5) | 140-180 h | 9/10 |
| 💼 | **MesaFácil — Reservas para restaurante o alojamiento rural** | Concurrencia de verdad: dos clientes, la última mesa, una sola reserva. | ●●●○○ (3/5) | 100-140 h | 10/10 |

## 3. Matriz de cobertura

`✔` = cubre el RA con peso · `~` = lo toca de forma opcional o secundaria · `–` = no aplica o hay que justificarlo

**🎮 Juegos en el navegador**

| Idea | `SI` | `SI-RA6` | `BD` | `ED` | `AD` | `PMDM·M` | `PMDM·MOV` | `DI` | `PSP` | `SGE` | Total |
|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 🂴 RiftDeck | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🏆 QuizArena | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🧩 CodeQuest | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| ♟️ HexArena | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 🏰 Escape360 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🤖 AutoClash | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |
| 🚀 PixelRaid | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ~ | **9** |
| 🌍 GeoSprint | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | **10** |

**💼 Otras ideas**

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

## 4. Juegos en el navegador

### 4.0 Antes de elegir: cómo se defiende un juego en un proyecto intermodular

Un juego es un proyecto **excelente**... siempre que no se quede en 'un canvas con sprites'. 
Estas son las reglas que marcan la diferencia entre un 4 y un 9:

- **El servidor es obligatorio.** Si todo ocurre en el navegador no hay PSP, no hay concurrencia real y la 'base de datos' es localStorage. Tu juego necesita servidor autoritativo: salas, temporizadores, validación de jugadas, ranking y persistencia. Es lo que convierte un juego en un proyecto de DAM.
- **El canvas no cubre DI por sí solo.** El RA de interfaces habla de interfaces interactivas, usabilidad y componentes (estándar o propios). Añade un **panel de administración / editor de contenidos / gestión de usuarios** con formularios, tablas, validación, accesibilidad y componentes propios: ahí está la mitad de la nota de DI.
- **La app móvil como companion cuenta (y mucho).** Notificaciones de turno, estadísticas, chat, tienda, retoques offline... Con la app haciendo algo real y sincronizado con el backend, el RA de móviles está cubierto sin tener que portar el juego entero.
- **El ERP-CRM entra por la monetización.** Tienda de cosméticos, sobres, licencias para centros o empresas, reservas de sesiones, patrocinios: con Odoo montas ventas, facturación y CRM, migras datos y verificas integridad. Mejor eso que un módulo de ERP metido con calzador.
- **Usa un motor, pero programa el juego.** Phaser, PixiJS, Three.js o Babylon son herramientas; lo evaluable es tu lógica: reglas, protocolo, servidor, persistencia y pruebas. Documenta en la memoria qué es del motor y qué es tuyo, con cifras (líneas de código propias, módulos, tests).
- **Los assets no son el proyecto.** Usa bancos libres (Kenney, OpenGameArt, Poly Pizza, freesound) y cítalos en los anexos. Nadie te va a puntuar por dibujar sprites, y te puedes dejar 40 horas en ello.
- **Mide y documenta el rendimiento.** Tick rate, salas concurrentes, speed-up de tu IA o simulador, latencia media, jugadores soportados en la prueba de carga: son capturas y gráficas directas para la memoria y para la defensa.
- **Cierra el alcance con un 'vertical slice'.** Un nivel, dos jugadores, tres mecánicas, un modo de juego. Un juego pequeño terminado y bien documentado puntúa mucho más que uno ambicioso a medias.
- **Cuidado con los menores y el RGPD.** Si el juego tiene registro, chat o ranking con menores de 14 años, documenta consentimiento, minimización de datos, retención y borrado. En un juego esto suma puntos en seguridad.
- **Graba un vídeo de la demo.** Los juegos en directo fallan el día de la defensa (red, latencia, un bug tonto). Ten siempre un vídeo corto y un servidor en local listo.

**Stack orientativo para juegos web**

| Pieza | Opción recomendada |
|-------|--------------------|
| 2D (el más recomendable) | Phaser 3 o PixiJS (canvas/WebGL) + TypeScript + Vite |
| 3D | Three.js o Babylon.js con modelos glTF |
| UI / menús / panel de admin | Vue 3, React o Svelte (el juego no tiene por qué ser solo canvas) |
| Servidor de salas | Node + Socket.IO / Colyseus, o Java + Netty / Spring WebSocket |
| Tiempo real | Snapshot a 15-20 Hz + interpolación + predicción del cliente |
| Audio | Web Audio API (música dinámica y pool de SFX) |
| Persistencia | PostgreSQL (+ Redis para estado caliente de sala y matchmaking) |
| Pruebas | Vitest/Jest para la lógica, bots de prueba y k6 o Artillery para carga |
| Despliegue | Docker + Nginx (TLS y proxy de WebSocket) + CI en GitHub Actions |
| Assets libres | Kenney, OpenGameArt, Poly Pizza, freesound.org (cítalos en los anexos) |

---

### 4.1 🂴 RiftDeck — Juego de cartas coleccionable online (TCG)

*Construyes tu mazo, juegas por turnos contra otro jugador y el servidor hace de árbitro.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 130-170 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | navegador, multijugador, por turnos, matchmaking, tienda |

**De qué va.** Juego de cartas por turnos en el navegador con dos frentes: el cliente de partida (tablero, mano, animaciones) y un panel web de gestión (editor de cartas, moderación, estadísticas). Detrás, un servidor autoritativo multihilo: una sala por partida, matchmaking por ELO, motor de reglas en el servidor, ranking y tienda. La app Android companion completa el círculo con la colección, los mazos y los avisos de torneo.

**Arquitectura (de un vistazo)**

- Servidor de salas: cada partida es una sala con su bucle de turnos en un hilo del pool; hilo propio para la cola de emparejamiento.
- Motor de reglas autoritativo: el cliente solo envía intenciones, el servidor valida y devuelve el estado (anti-trampas natural).
- API REST + WebSocket (Socket.IO) para acciones de partida, chat y presencia.
- Cliente web: Phaser 3 o PixiJS para el tablero; Vue/React para login, tienda y menús.
- PostgreSQL (jugadores, cartas, mazos, partidas, transacciones) + Redis (matchmaking y presencia) + Odoo (tienda y facturación).

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | Phaser 3 + TypeScript (o PixiJS) + Vite |
| UI / menús | Vue 3 + Pinia + Tailwind |
| Servidor | Node + Colyseus/Socket.IO (o Java + Netty si prefieres PSP en Java) |
| Datos | PostgreSQL + Redis |
| Móvil | Kotlin + Room + FCM |
| ERP | Odoo Community (Tienda, Ventas, Facturación, CRM) |
| Infra | Debian + Docker + Nginx (TLS + proxy WebSocket) + copias |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Despliegue en Linux con Docker, Nginx con TLS y proxy de WebSockets, servicios con systemd, copias automáticas y monitorización de salas activas. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Servidor autoritativo (el cliente no decide nada), JWT con 2FA, rate limiting, validación de cada acción, protección de la economía virtual, RGPD y menores, y registro de auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo jugadores-cartas-mazos-partidas-transacciones; la joya es la economía: transacciones que impiden gastar dos veces el mismo recurso, histórico de partidas y copias verificadas. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | Monorepo con workspaces, CI (lint, test, build), entornos dev/staging/prod y pruebas automatizadas del motor de reglas y del emparejamiento. |
| ✔ **Acceso a datos** (`AD`) | Capa ORM/DAO, consultas de ranking paginadas, exportación de replays en JSON y cliente de la API del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Sprites y animaciones de cartas, efectos de partículas al invocar, música y SFX con WebAudio, transiciones y generación de las imágenes del catálogo de cartas. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android companion: consulta colección y mazos, recibe notificaciones de torneos y de turno pendiente, chat de amigos y recompensa diaria con trabajo en segundo plano. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mucho más que un canvas: login y registro, editor de mazos drag&drop con filtros, tienda, panel de administración y componentes propios (carta con estados, contador de turnos, tooltip de habilidades). |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Cada partida vive en una sala con su propio bucle de turnos dentro de un pool, más un hilo de emparejamiento y workers de ranking y cierre de temporada. Hay estado compartido que hay que sincronizar de verdad: es PSP de manual. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para la tienda (sobres, cosméticos), pedidos, facturación y CRM de jugadores con campañas de retención; migración de datos y verificación de integridad. |

**Por qué mola**

- Es el juego que más parece un producto real: economía, matchmaking, ranking, tienda y temporadas.
- Al ser por turnos no te peleas con el netcode de precisión, y aun así el PSP es fortísimo.
- Demo facilísima: abres dos pestañas (o un móvil) y juegas contra ti mismo en directo.

**Riesgos y cómo mitigarlos**

- El motor de reglas crece sin control: define 20-30 cartas y 3 mecánicas, y documenta el resto como 'líneas futuras'.
- El arte puede comerte horas: usa assets libres (Kenney, OpenGameArt) y cítalos en los anexos.
- Cuidado con clonar Hearthstone: cambia temática y mete una mecánica propia para que sea defendible.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | 20 cartas y reglas básicas; Partida 1v1 por WebSocket; Login y ranking; Matchmaking simple |
| Fase 2 | Editor de mazos drag&drop; Tienda y moneda virtual; App companion; Chat y amigos |
| Fase 3 | ELO y temporadas; Replays; Integración con Odoo; Panel de moderación |

---

### 4.2 🏆 QuizArena — Concurso multijugador en directo

*El presentador lanza la pregunta, veinte móviles responden a la vez y el marcador sube en vivo.*

| | |
|---|---|
| Dificultad | ●●●○○ (3/5) |
| Esfuerzo estimado | 100-140 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | navegador, tiempo real, móvil, aulas, demoable |

**De qué va.** Juego de preguntas en directo para aulas, empresas y eventos. El presentador conduce el concurso desde un panel con pantalla proyectable; los jugadores entran con un código desde el móvil o el navegador y responden con límite de tiempo. El servidor mantiene muchas salas concurrentes con temporizadores precisos, puntúa por velocidad y emite el marcador en vivo. Preguntas con imagen, audio y vídeo, informes PDF por sesión y licencias facturadas en el ERP.

**Arquitectura (de un vistazo)**

- Servidor de salas concurrentes: hilo por sala para el temporizador de pregunta y broadcast por WebSocket.
- Panel del presentador (web o app de escritorio con Tauri) con pantalla proyectable y control de ritmo.
- Cliente del jugador: web responsive + app Android nativa con notificaciones e historial.
- BD de preguntas por categorías con multimedia adjunta; generación de informes y diplomas PDF.
- ERP: centros y empresas, licencias, facturación recurrente y CRM.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | Vue 3 + Canvas/CSS para animaciones (o Phaser 3 si quieres más juego) |
| Presentador | Web + proyección a pantalla completa, o empaquetado con Tauri |
| Servidor | Node + Socket.IO (o Spring Boot + WebSocket) con pool de salas |
| Móvil | Kotlin + FCM + Room |
| Datos | PostgreSQL + Redis (salas en memoria) |
| ERP | Odoo Community (Ventas, Suscripciones, CRM) |
| Infra | Linux + Docker + Nginx + bots de prueba para carga |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Despliegue con Docker + Nginx + TLS, WebSockets, copias automáticas y monitorización; prueba de carga con 100 jugadores simulados. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Códigos de sala con caducidad, JWT, rate limit anti-spam, validación en servidor del instante de respuesta (anti-trampas), RGPD y menores. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo cuestionarios-preguntas-sesiones-respuestas con integridad referencial, transacciones al cerrar cada ronda y estadísticas de acierto. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, pruebas end-to-end del flujo de partida con bots, entornos separados y empaquetado del panel con Tauri. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas de ranking y estadísticas por sesión, exportación de resultados y cliente de la API del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Preguntas con imagen, audio y vídeo; cuenta atrás sonora, animaciones de acierto/fallo y diplomas en PDF. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android del jugador: entra con código, responde, ve el resultado y recibe avisos de próximos concursos; modo repaso offline. |
| ✔ **Desarrollo de interfaces** (`DI`) | Pantalla del presentador, marcador en vivo y panel de gestión de preguntas con componentes animados propios (barra de tiempo, podio, racha de aciertos). |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Decenas de salas simultáneas, cada una con su temporizador y su broadcast, más workers de cálculo de ranking y de generación de informes: concurrencia con sentido y medible. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para centros y empresas: licencias, suscripciones, facturación recurrente y CRM con informes de uso. |

**Por qué mola**

- La defensa se monta sola: el tribunal saca el móvil, mete el código y juega en directo.
- Es el más barato de desarrollar y el más demoable de toda la lista.
- Encaja en un caso real (tu centro, empresas de formación, eventos) sin inventarte nada.

**Riesgos y cómo mitigarlos**

- Es 'el típico Kahoot': diferénciate con el modo torneo, los informes y las licencias en el ERP.
- Los temporizadores en red son delicados: el reloj lo manda el servidor y se compensa la latencia (documéntalo, es material de memoria).
- Necesitas contenido: crea 3 cuestionarios de 20 preguntas y un importador CSV.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Salas con código; Pregunta con temporizador; Marcador en vivo; Panel del presentador |
| Fase 2 | Preguntas multimedia; App móvil; Informes PDF; Ranking global |
| Fase 3 | Modo torneo; Importador CSV; Licencias en Odoo; Bots y pruebas de carga |

---

### 4.3 🧩 CodeQuest — Retos de lógica gamificados (y ejecutor en sandbox)

*Resuelves retos en el navegador, subes de nivel y compites con tu clase.*

| | |
|---|---|
| Dificultad | ●●●○○ (3/5) |
| Esfuerzo estimado | 110-150 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | navegador, gamificación, sandbox, educativo, seguridad |

**De qué va.** Plataforma de aprendizaje gamificada: el alumno resuelve retos de lógica (puzles de bloques, laberintos, pequeños programas) en un cliente web 2D, con niveles, logros, rachas y ranking por clase. El profesor crea itinerarios y ve analítica de progreso. La parte técnica estrella: las soluciones se ejecutan y validan en workers aislados con límite de tiempo y memoria, y el ERP-CRM gestiona centros, licencias y facturación.

**Arquitectura (de un vistazo)**

- Cliente web: Phaser 3 o PixiJS para los retos, Vue/React para menús, perfil y progreso.
- Servidor: API REST + WebSocket y un ejecutor de soluciones en procesos aislados (sandbox) con cola y límite de workers.
- Motor de gamificación en servidor: puntos, logros, rachas y niveles (para que no se puedan falsear).
- Panel del profesor con analítica, itinerarios y exportación de informes.
- ERP: centros educativos, licencias, facturación y CRM.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | Phaser 3 o PixiJS + Vue 3 |
| Servidor | Node o Python (FastAPI) + cola de trabajos |
| Ejecución aislada | Procesos con límites (ulimit/cgroups) o contenedores efímeros |
| Datos | PostgreSQL + Redis |
| Móvil | Kotlin + Room + FCM |
| ERP | Odoo Community (Ventas, Suscripciones, CRM) |
| Infra | Linux + Docker + Nginx + monitorización de la cola |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux con Docker, Nginx, cola de trabajos, copias y monitorización del consumo de la cola. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | El sandbox es oro: límites de tiempo/memoria, sin red y sin disco, validación en servidor; además JWT, roles y RGPD con menores de edad (dato sensible). |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo alumnos-retos-intentos-logros con integridad referencial, histórico de intentos y agregados para la analítica. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI con pruebas del evaluador, versionado del formato de retos, entornos separados y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas de progreso y ranking, exportación de datos y cliente del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Gráficos 2D de los retos, animaciones de logros, efectos de sonido y generación de diplomas PDF. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android para repasar retos cortos, mantener la racha con notificaciones y consultar el progreso sin conexión. |
| ✔ **Desarrollo de interfaces** (`DI`) | Panel del profesor, perfil del alumno con progreso visual, editor de itinerarios drag&drop y componentes propios de puzle y de logro. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | La cola de ejecución con workers concurrentes, timeouts, cancelación y límites de CPU es multiproceso de verdad, con un riesgo real que hay que controlar y documentar. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para centros educativos, licencias por alumno, facturación y CRM; verificación de integridad tras la migración. |

**Por qué mola**

- Tiene impacto real: puedes usarla con tus propios compañeros y el tribunal lo ve funcionando.
- El sandbox de ejecución es un problema técnico duro que te da PSP y seguridad a la vez.
- El alcance se recorta facilísimo sin que el proyecto se quede cojo.

**Riesgos y cómo mitigarlos**

- Ejecutar código de alumnos es peligroso: empieza con retos de bloques/lógica, y si ejecutas código, aísla de verdad (y cuéntalo en la memoria).
- Riesgo de 'otra plataforma educativa más': el centro del proyecto es el juego y la gamificación.
- La analítica crece sin parar: limita a cuatro gráficas bien hechas.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | 5-8 retos jugables; Sistema de niveles y logros; Panel del profesor; Ranking por clase |
| Fase 2 | Ejecutor sandbox de soluciones; Editor de itinerarios; App móvil de repaso; Informes PDF |
| Fase 3 | Analítica avanzada; Licencias en Odoo; Modo competición entre clases |

---

### 4.4 ♟️ HexArena — Estrategia por turnos con IA que piensa en paralelo

*Un juego de estrategia donde la IA calcula en varios hilos a la vez y puedes medir cuánto gana.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 120-160 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | navegador, IA, multihilo, por turnos, medible |

**De qué va.** Juego de estrategia por turnos en el navegador (batallas en tablero hexagonal) contra otros jugadores o contra la IA. La búsqueda de jugadas (minimax con poda alfa-beta o MCTS) se reparte en un pool de hilos/procesos en el servidor, con control de tiempo y una comparativa secuencial vs concurrente que es material directo para la memoria. Incluye matchmaking, ELO, repeticiones de partidas y editor de mapas.

**Arquitectura (de un vistazo)**

- Cliente web: PixiJS/Phaser o Canvas para el tablero hexagonal; UI en Vue/React.
- Servidor: una sala de partida por hilo, servicio de IA con pool de workers y cola de trabajos con timeout.
- Módulo de medidas: tiempos secuencial frente a paralelo y gráfica de speed-up para la documentación.
- BD con partidas, movimientos y repeticiones; Redis para matchmaking y presencia.
- App móvil para partidas asíncronas ('por correspondencia') con notificación de turno.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | PixiJS o Phaser 3 + TypeScript |
| Servidor | Java (ExecutorService/ForkJoin) o Node con worker_threads |
| IA | Minimax con poda alfa-beta / MCTS, con límite de tiempo |
| Datos | PostgreSQL + Redis |
| Móvil | Kotlin + FCM + Room |
| Infra | Linux + Docker + Nginx + benchmark automático |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, contenedores, Nginx con WebSockets, copias y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Servidor autoritativo de reglas, validación de cada movimiento, JWT, límites de tiempo de turno, anti-trampas y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo partidas-movimientos-repeticiones con integridad, transacción por turno, histórico y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI con pruebas del motor de IA, benchmarks automáticos del speed-up, entornos y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas de historial y ranking, serialización de repeticiones y exportación. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Sprites de unidades, animaciones de ataque, partículas, sonido y miniaturas de mapa generadas. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android de partidas asíncronas: te toca el turno, te llega la notificación y juegas desde el móvil sin pelearte con el tiempo real. |
| ✔ **Desarrollo de interfaces** (`DI`) | Tablero interactivo como componente propio (hit-testing hexagonal), menús, editor de mapas y visor de repeticiones con controles de reproducción. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | El mejor escaparate de la lista: pool de hilos para buscar jugadas, salas concurrentes, cancelación por timeout, secciones críticas y una gráfica de speed-up que demuestra el multihilo con números. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: Odoo para torneos, inscripciones, premios y facturación de patrocinios. |

**Por qué mola**

- Es el proyecto donde el multihilo se ve, se mide y se defiende con una gráfica en la memoria.
- Sin arte complejo: con sprites sencillos queda precioso y todo el esfuerzo va al código.
- El modo asíncrono te da notificaciones móviles sin complicarte con netcode.

**Riesgos y cómo mitigarlos**

- Una IA decente consume horas: fija profundidad, poda y tiempo máximo de cómputo.
- Evita el tiempo real como MVP: el modo asíncrono es suficiente y más seguro.
- Riesgo de 'clon del ajedrez': diseña reglas propias (unidades, recursos, mapa, condiciones de victoria).

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Tablero hexagonal jugable; Reglas de 3-4 unidades; IA secuencial con profundidad fija; Partida contra IA |
| Fase 2 | IA paralela con pool de hilos y medición; Multijugador asíncrono; App móvil de turnos; Editor de mapas |
| Fase 3 | Matchmaking y ELO; Repeticiones; Torneos; Integración ERP opcional |

---

### 4.5 🏰 Escape360 — Escape room cooperativo en 3D en el navegador

*Varias personas dentro de la misma habitación 3D, moviéndose a la vez y resolviendo puzles en equipo.*

| | |
|---|---|
| Dificultad | ●●●●● (5/5) |
| Esfuerzo estimado | 140-180 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | navegador, 3D, cooperativo, editor, multimedia |

**De qué va.** Escape room cooperativo en primera persona con Three.js o Babylon.js: hasta 4 jugadores simultáneos en la misma sala, sincronización de posición e inventario, puzles encadenados y chat de equipo. Un editor web permite al monitor crear salas, colocar objetos y definir puzles sin programar. El servidor mantiene el estado de cada sala en su hilo, y el ERP-CRM gestiona las reservas de empresas y la facturación de sesiones.

**Arquitectura (de un vistazo)**

- Cliente 3D: Three.js o Babylon.js con modelos glTF, iluminación, colisiones y audio espacial (WebAudio).
- Servidor de salas multihilo: estado compartido de la sala, sincronización de posiciones a 15-20 Hz y validación de puzles.
- Editor de salas: colocación de objetos, definición de puzles y exportación a JSON versionado.
- Chat de equipo (y voz por WebRTC como extra).
- ERP: empresas clientas, reservas de sesión, facturación y CRM.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente 3D | Three.js o Babylon.js + TypeScript |
| UI y editor | Vue 3 + inspector de propiedades |
| Servidor | Node + Socket.IO (o Colyseus) con salas en hilos |
| Assets | Modelos glTF libres (Kenney, Poly Pizza, Sketchfab CC) |
| Datos | PostgreSQL + Redis (estado de sala) |
| ERP | Odoo Community (Ventas, Reservas, Facturación, CRM) |
| Infra | Linux + Docker + Nginx + TURN propio para WebRTC |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Despliegue con Docker, Nginx con TLS, WebSockets y TURN, copias y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Validación de puzles en servidor, JWT, salas privadas con código y caducidad, RGPD y auditoría de sesiones. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo salas-objetos-puzles-sesiones-reservas con integridad referencial, transacciones de reserva y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, pruebas del editor y del formato de sala, entornos y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM, persistencia de sesiones y resultados, exportación de salas a JSON y cliente del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | El más fuerte de todos en multimedia: modelos 3D, texturas, iluminación, animaciones, audio espacial y efectos de postproceso. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android como mando del jugador: inventario, pistas, chat y notificaciones de sesión (o visor móvil de la sala). |
| ✔ **Desarrollo de interfaces** (`DI`) | El editor de salas es un producto dentro del producto: drag&drop, capas, inspector de propiedades y guardado/versionado. Ahí se defiende DI sin discusión. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Una sala cooperativa por hilo con estado compartido entre jugadores, cola de mensajes, workers de validación de puzles y temporizador de sesión. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para empresas clientas: reservas de sesiones de team building, facturación y CRM; verificación de integridad. |

**Por qué mola**

- Técnicamente el más ambicioso y el que más impresiona en pantalla grande.
- El editor de salas te salva el RA de interfaces: es una aplicación de gestión dentro del juego.
- Se puede plantear como negocio real de escape rooms para empresas.

**Riesgos y cómo mitigarlos**

- El 3D en el navegador es carísimo en tiempo: una sola sala bien hecha y assets gratuitos.
- Sincronizar jugadores es lo más difícil: empieza con 2 jugadores y 15 Hz.
- Rendimiento en equipos modestos: perfil gráfico automático y modelo de baja poligonización.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Una sala 3D navegable; 2 jugadores sincronizados; 2-3 puzles encadenados; Chat de equipo |
| Fase 2 | Editor de salas; Inventario compartido; App mando; Audio espacial |
| Fase 3 | 4 jugadores; Reservas y facturación en Odoo; Voz por WebRTC |

---

### 4.6 🤖 AutoClash — Auto-battler por rondas con simulación en el servidor

*Compras unidades y colocas el tablero; el combate lo simula el servidor en paralelo y lo ves como replay.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 120-160 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | navegador, multijugador, simulación, determinismo, temporadas |

**De qué va.** Auto-battler multijugador: 8 jugadores compran y colocan unidades durante una fase de preparación con tiempo límite; al cerrar, el servidor simula todos los combates a la vez en un pool de workers y devuelve el resultado como una replay animada en el cliente web. Temporadas, ranking, tienda rotatoria y cosméticos. La clave técnica: el simulador es determinista por semilla, así que se puede reproducir, verificar y testear.

**Arquitectura (de un vistazo)**

- Servidor: salas de 8 jugadores con temporizador de fase (hilo por sala) y simulador determinista ejecutado en un pool de workers.
- Cliente web: Phaser/PixiJS para el tablero y la reproducción de combates; Vue/React para tienda y perfil.
- Sistema de temporadas, ranking y cosméticos con tienda conectada al ERP.
- App móvil companion: estadísticas, cola, historial de combates y avisos de temporada.
- Suite de tests que reproduce combates a partir de la semilla (regresión y anti-trampas).

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | Phaser 3 o PixiJS + TypeScript |
| Servidor | Java (pool de hilos) o Node con worker_threads |
| Simulador | Lógica determinista con semilla + PRNG propio (nada de Math.random) |
| Datos | PostgreSQL + Redis |
| Móvil | Kotlin + Room + FCM |
| ERP | Odoo Community (Tienda, Facturación, CRM) |
| Infra | Linux + Docker + Nginx + pruebas de carga del simulador |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Docker, Nginx + WebSockets, copias, monitorización y pruebas de carga del simulador. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | El cliente no puede mentir porque no simula nada: determinismo verificable por semilla, JWT, rate limit y auditoría de resultados. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo temporadas-partidas-rondas-compras con integridad de la economía (transacciones al comprar y vender unidades) y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI con tests del simulador (combates reproducibles), benchmarks de workers, entornos y empaquetado. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas de ranking y metadatos de temporada, serialización de combates y cliente del ERP. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Sprites y animaciones de combate, efectos, sonido, y generación de miniaturas de composición para el historial. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App companion con estadísticas de temporada, historial de combates y notificaciones de inicio de ronda. |
| ✔ **Desarrollo de interfaces** (`DI`) | Tablero de preparación drag&drop, tienda rotatoria, panel de administración de temporadas y componentes propios de unidad y barra de vida. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Ocho combates simulados a la vez en un pool de workers, con semillas, reintentos, cancelación por timeout y medición de rendimiento: concurrencia que se justifica sola. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para la tienda de cosméticos, pedidos, facturación y CRM de jugadores. |

**Por qué mola**

- Todo el juego ocurre en el servidor: es el anti-trampas y el argumento de PSP en uno.
- Las replays te dan demo garantizada aunque el tribunal no sepa jugar.
- Sin netcode de precisión: solo hay que sincronizar el inicio y el final de cada ronda.

**Riesgos y cómo mitigarlos**

- El balance consume horas: 8-10 unidades y 3 sinergias, ni una más.
- El determinismo exige disciplina (nada de Math.random ni depender del orden de un mapa): documéntalo, es oro para la memoria.
- Arte: assets libres y una paleta coherente, no sprites hechos a mano.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Tablero y 8 unidades; Fase de preparación con temporizador; Simulador determinista; Replay del combate |
| Fase 2 | 8 jugadores por sala; Economía y tienda; Pool de workers y medición; Ranking |
| Fase 3 | Temporadas y cosméticos; App companion; Tienda en Odoo |

---

### 4.7 🚀 PixelRaid — Arcade cooperativo en tiempo real (servidor autoritativo)

*Disparas en el navegador y el servidor decide si has acertado: netcode de verdad.*

| | |
|---|---|
| Dificultad | ●●●●● (5/5) |
| Esfuerzo estimado | 150-190 h |
| Bloques cubiertos | 9/10 |
| Etiquetas | navegador, tiempo real, netcode, servidor autoritativo, arriesgado |

**De qué va.** Arcade cooperativo multijugador en tiempo real (bullet-hell por oleadas) con servidor autoritativo: bucle de simulación a 30 Hz por sala, predicción del lado del cliente, interpolación de entidades remotas y reconciliación de estado. Incluye progresión persistente, ranking semanal, salas privadas y un panel de administración con métricas en vivo del servidor (tick rate, latencia, salas activas).

**Arquitectura (de un vistazo)**

- Servidor: bucle de simulación por sala (hilo por sala), snapshots a 20 Hz y comandos de entrada del cliente.
- Cliente web: Phaser 3 o PixiJS con predicción de movimiento e interpolación; HUD y lobby.
- Servicio de métricas y logging de partidas; ranking semanal y progresión persistente.
- Panel de administración con salas en vivo, expulsiones y gráficas de latencia y ticks.
- Bots de prueba para generar carga y demostrar la concurrencia.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Cliente web | Phaser 3 o PixiJS + TypeScript |
| Servidor | Node + Socket.IO (UDP si te atreves) o Java + Netty |
| Red | Snapshots + interpolación + reconciliación (predicción del cliente) |
| Datos | PostgreSQL + Redis (estado caliente de sala) |
| Móvil | Kotlin companion (estadísticas, ranking, invitaciones) |
| Infra | Linux + Docker + Nginx + monitorización de tick rate |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, Docker, Nginx, WebSockets, monitorización del tick rate y copias. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Servidor autoritativo, validación de movimiento y disparo, límites de tasa, detección de speedhack, JWT y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | Modelo jugadores-partidas-oleadas-progresión con integridad referencial, transacciones al guardar progresión y copias. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, tests de simulación determinista, entornos, empaquetado y pruebas de carga con bots. |
| ✔ **Acceso a datos** (`AD`) | ORM, consultas de ranking y progresión, persistencia de métricas por partida. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Sprites animados, partículas, screen shake, música dinámica y pool de efectos de sonido con WebAudio. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | App Android companion: ranking semanal, estadísticas, lista de amigos y notificaciones de invitación a sala. |
| ✔ **Desarrollo de interfaces** (`DI`) | HUD de partida, lobby, salas privadas y un panel de administración en vivo con gráficas reales de latencia y ticks por segundo. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Varios bucles de simulación concurrentes, uno por sala, con sincronización, control de tick rate y backpressure: el PSP más exigente y el más demostrable de la lista. |
| ~ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Opcional: Odoo para cosméticos y pases de temporada, facturación y CRM. |

**Por qué mola**

- Es el proyecto 'juego' por excelencia: si te va el netcode, este es tu sitio.
- El panel de administración con métricas en vivo defiende SI y DI de un tirón.
- La progresión persistente te da base de datos y economía real.

**Riesgos y cómo mitigarlos**

- Es el mayor riesgo de la lista: fija el MVP en 2 jugadores, 20 Hz y un solo nivel.
- Sin bots de prueba no puedes demostrar carga ni concurrencia: hazlos desde el principio.
- Latencia en la defensa: ten el servidor en local y un replay grabado como plan B.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | Bucle de simulación en servidor; 1 nivel y 2 jugadores; Predicción e interpolación; HUD y lobby |
| Fase 2 | Oleadas y progresión; Salas privadas; Panel de administración en vivo; Bots de carga |
| Fase 3 | Ranking semanal; App companion; Cosméticos y tienda en Odoo |

---

### 4.8 🌍 GeoSprint — Captura territorial por GPS (móvil + mapa web en vivo)

*El juego vive en tu bolsillo; el navegador es el mapa que se pinta en directo.*

| | |
|---|---|
| Dificultad | ●●●●○ (4/5) |
| Esfuerzo estimado | 130-170 h |
| Bloques cubiertos | 10/10 |
| Etiquetas | móvil, GPS, mapas, concurrencia, navegador |

**De qué va.** Juego de captura territorial por GPS: la app Android es el cliente principal (mapa, localización en segundo plano, captura de zonas, cámara/AR opcional) y el navegador muestra el mapa global en vivo consumiendo el mismo backend. El servidor ingesta posiciones, resuelve capturas concurrentes sobre la misma zona con transacciones y bloqueos, aplica geocercas y lleva las temporadas por barrios. El ERP-CRM gestiona patrocinios locales y su facturación.

**Arquitectura (de un vistazo)**

- App Android: Fused Location en servicio en primer plano, mapas, captura de zonas y cola de acciones offline.
- Servidor: ingesta de posiciones por WebSocket/HTTP, resolución concurrente de capturas (lock por zona + transacción), temporadas.
- Cliente web: mapa global en vivo (Leaflet/MapLibre) y panel de administración de zonas.
- BD espacial (PostGIS) y series de posiciones con retención.
- Simulador de rutas GPX para poder demostrar el juego sin salir del aula.

**Stack sugerido**

| Pieza | Tecnología |
|-------|------------|
| Móvil | Kotlin + Google Maps / MapLibre + Fused Location + Room |
| Cliente web | Vue 3 + MapLibre/Leaflet |
| Servidor | Spring Boot o Node con WebSockets |
| Datos | PostgreSQL + PostGIS |
| ERP | Odoo Community (Ventas, Facturación, CRM) |
| Infra | Linux + Docker + Nginx + simulador GPX |

**Cómo cubre cada RA**

| Bloque | Cómo lo justificas |
|--------|--------------------|
| ✔ **Configuración y explotación de sistemas** (`SI`) | Servidor Linux, Docker, Nginx con TLS, copias y monitorización. |
| ✔ **Seguridad en sistemas, servicios y aplicaciones** (`SI-RA6`) | Detección básica de GPS falso (saltos imposibles, velocidad irreal), JWT, privacidad de la ubicación (RGPD) y auditoría. |
| ✔ **Gestión de bases de datos** (`BD`) | PostGIS con datos espaciales, integridad de capturas, transacciones y control de concurrencia por zona; copias y retención. |
| ✔ **Gestión de entornos de desarrollo** (`ED`) | CI, pruebas de geocercas y de resolución de capturas, entornos y empaquetado de la app. |
| ✔ **Acceso a datos** (`AD`) | Consultas espaciales, ORM, cliente del ERP y exportación de datos de temporada. |
| ✔ **Contenidos multimedia** (`PMDM·M`) | Tiles de mapa, marcadores animados, captura con cámara y generación de imágenes de cierre de temporada. |
| ✔ **Dispositivos móviles** (`PMDM·MOV`) | El rey del RA de móviles: localización continua en segundo plano, mapas, cámara, notificaciones, permisos y sincronización offline de acciones. |
| ✔ **Desarrollo de interfaces** (`DI`) | Mapa global en vivo con capas, filtros y leyenda (componente propio), más el panel de administración de zonas y sus estadísticas. |
| ✔ **Servicios y procesos (multiproceso / multihilo)** (`PSP`) | Ingesta concurrente de posiciones, workers de resolución de capturas con bloqueo por zona y temporizadores de temporada: condiciones de carrera reales con impacto en el juego. |
| ✔ **Sistemas de gestión empresarial (ERP-CRM)** (`SGE`) | Odoo para patrocinadores locales (comercios que patrocinan zonas), contratos, facturación y CRM. |

**Por qué mola**

- Es el único donde el móvil es el protagonista y el navegador es el marcador global.
- Muy visual en la defensa: el mapa cambia de color en directo mientras juegas.
- El conflicto de dos capturas simultáneas es un problema de BD y PSP perfecto de explicar.

**Riesgos y cómo mitigarlos**

- Para probarlo de verdad hay que salir a la calle: haz un simulador de rutas GPX para la demo.
- Batería y permisos de ubicación en segundo plano: documéntalo como decisión de diseño.
- ARCore añade mucho riesgo: déjalo para la fase 3 o descártalo sin pena.

**Alcance por fases (corta aquí si te falta tiempo)**

| Fase | Entregable |
|------|------------|
| MVP | App con mapa y posición; Zonas y captura; Mapa web en vivo; Ranking |
| Fase 2 | Resolución concurrente de capturas; Geocercas y temporadas; Modo offline; Simulador GPX |
| Fase 3 | Equipos y ligas; Patrocinios en Odoo; Cámara/AR |

## 5. Otras ideas (por si cambias de rumbo)

No son juegos, pero están aquí por si en algún momento te replanteas el enfoque y quieres comparar.

---

### 5.1 🎥 SentinelVIS — Tu propio NVR de videovigilancia IP

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

### 5.2 📦 LogiScan — Almacén con PDA, códigos de barras y RFID

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

### 5.3 🏋️ GymCore — ERP-CRM de gimnasio con app de socio y multimedia

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

### 5.4 🛡️ NetSentinel — Monitorización de red y mini-SOC

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

### 5.5 🍿 StreamHub — Servidor multimedia y streaming (estilo Plex propio)

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

### 5.6 🚚 FleetTrack — Flota y reparto con seguimiento GPS en vivo

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

### 5.7 🎫 HelpDesk Pro — Gestión de incidencias con SLA y app de técnico

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

### 5.8 📄 DocuFlow — Digitalización certificada y gestor documental con OCR

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

### 5.9 🏠 EcoDomus — Domótica y control de accesos con Raspberry Pi

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

### 5.10 🍽️ MesaFácil — Reservas para restaurante o alojamiento rural

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

## 6. Recomendación según tu perfil

**→ Si quieres el juego más completo y defendible: RiftDeck — Juego de cartas coleccionable online (TCG)**

Es el que más parece un producto real (mazos, matchmaking, ranking, economía, tienda) y, al ser por turnos, no te vas a estrellar con el netcode. Cubre los 10 bloques y la demo son dos pestañas jugando entre sí. Si tengo que elegir uno por ti, es este.

**→ Si quieres el juego más fácil de defender en la sala: QuizArena — Concurso multijugador en directo**

El tribunal juega con su propio móvil en 30 segundos: es la demo más agradecida que existe y la más barata de desarrollar. El riesgo es que parezca 'un Kahoot', así que apóyate en el modo torneo, los informes y las licencias en el ERP.

**→ Si quieres lucirte en PSP (multihilo): HexArena — Estrategia por turnos con IA que piensa en paralelo**

La IA buscando jugadas en un pool de hilos, con una gráfica de speed-up en la memoria, es la demostración de multihilo más limpia y medible de toda la lista. Sin arte complejo y con modo asíncrono para la app móvil.

**→ Si quieres el juego más espectacular: Escape360 — Escape room cooperativo en 3D en el navegador**

Un escape room 3D cooperativo en el navegador impresiona en pantalla grande, y el editor de salas te salva el RA de interfaces. Es el más arriesgado: solo si tienes margen de tiempo y te apetece pelearte con el 3D.

**→ Si te mola de verdad el multijugador en tiempo real: PixelRaid — Arcade cooperativo en tiempo real (servidor autoritativo)**

Servidor autoritativo, snapshots, predicción e interpolación: netcode de verdad. Es el proyecto más difícil y el que más puede lucir... o el que más rápido se desborda. Solo con bots de prueba desde el día uno.

**→ Si quieres que el móvil pese en el proyecto: GeoSprint — Captura territorial por GPS (móvil + mapa web en vivo)**

Aquí la app Android es el cliente principal (GPS, mapas, segundo plano, modo offline) y el navegador es el mapa global en vivo. Es el juego que mejor encaja con el RA de dispositivos móviles.

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

## 7. Ideas rápidas (plan B)

Proyectos más pequeños por si tu centro te limita el alcance o vas justo de tiempo.

| Tipo | Idea | Qué aporta | Bloques que cubre |
|:----:|------|------------|-------------------|
| 🎮 | **Ajedrez online multijugador con ELO** | Tablero en canvas + WebSocket, salas, ELO y chat. Fácil de acotar, pero muy visto: añade variante propia o torneos. | `DI`, `PSP`, `BD`, `AD` |
| 🎮 | **Roguelike de navegador con ranking semanal** | Una sola mecánica bien pulida, semillas compartidas y tabla de clasificación. Puro Phaser 3 + servidor ligero. | `PMDM·M`, `DI`, `PSP`, `BD` |
| 🎮 | **Tower defense cooperativo por oleadas** | Dos jugadores colocan torres y el servidor simula las oleadas. Menos netcode que un shooter y muy vistoso. | `PSP`, `DI`, `PMDM·M`, `BD` |
| 💼 | **Préstamo de equipos del centro (aulas/material)** | App móvil con escaneo de códigos de barras, escritorio para el conserje y control de incidencias. Pequeño, cerrado y 100% terminable. | `PMDM·MOV`, `AD`, `DI`, `BD` |
| 💼 | **Clon de Spotify para el catálogo de audio del ciclo** | Podcasts y audios propios, streaming multihilo, app móvil con reproducción offline y panel de subida. | `PMDM·M`, `PSP`, `PMDM·MOV`, `DI` |
| 💼 | **Generador automático de horarios escolares** | Algoritmo con restricciones ejecutado en varios hilos, interfaz para fijar restricciones y exportación a PDF/Excel. | `PSP`, `DI`, `PMDM·M`, `BD` |
| 💼 | **Sistema de control de presencia con reconocimiento facial** | Captura con OpenCV, comparación de embeddings, panel de escritorio y justificantes. Ojo con RGPD: datos sintéticos. | `PMDM·M`, `SI-RA6`, `PSP`, `DI` |
| 💼 | **Simulador de bolsa con datos en tiempo real** | Ingesta multihilo de datos de mercado, gráficas en vivo, carteras y alertas móviles. Sin dinero real. | `PSP`, `DI`, `PMDM·MOV`, `AD` |
| 💼 | **Plataforma de tutorías y seguimiento académico** | Citas, chat multihilo, informes PDF con gráficas y app móvil con recordatorios. Encaja bien con un centro educativo real. | `DI`, `PSP`, `PMDM·MOV`, `PMDM·M` |

## 8. Checklist de elección

Antes de cerrar la idea, responde honestamente:

1. ¿Cubre al menos 6-7 de los 9 bloques de RAs sin inventarte funcionalidades que nadie pediría?
2. ¿Tienes una demo que se vea en 2 minutos y que falle poco el día de la defensa?
3. ¿Puedes recortar el 30% del alcance y que siga teniendo sentido? (si no, el alcance es excesivo)
4. ¿El ERP-CRM tiene encaje real o lo estás metiendo con calzador? (si es con calzador, el tribunal lo nota)
5. ¿Hay un problema técnico 'duro' (concurrencia, multimedia, tiempo real) que luzcas en PSP o PMDM?
6. ¿Puedes generar datos de prueba creíbles sin depender de terceros?
7. ¿Te apetece de verdad? Vas a echarle muchas horas.

## 9. Estructura propuesta de la memoria

1. Introducción: contexto, problema, motivación y por qué este proyecto (aquí vendes el 'chulo').
2. Análisis: estudio de alternativas existentes, requisitos funcionales y no funcionales, casos de uso, actores, prototipos de interfaz.
3. Diseño: arquitectura (diagrama de componentes y despliegue), modelo de datos (ER y relacional), diseño de interfaces, protocolos, seguridad y plan de seguridad.
4. Planificación y presupuesto: estimación, diagrama de Gantt, costes de hardware, software y horas (EIE).
5. Implementación y verificación: entornos de desarrollo, control de versiones, pruebas (unitarias, integración, carga, usabilidad) y resultados.
6. Implantación: manual de instalación, configuración del servidor, copias de seguridad y plan de seguridad aplicado.
7. Conclusiones y líneas futuras.
8. Anexos: manual de usuario (escritorio y móvil), manual de administración/instalación, código fuente (enlace al repositorio), diccionario de datos, guion de la demo y capturas.

## 10. Trampas clásicas

- Un CRUD con login: no llega, por mucho que le pongas gráficas.
- Depender de una API externa que puede caerse o cambiar el día de la defensa: ten siempre datos en local.
- Meter el ERP porque 'hay que meterlo': si no hay migración de datos ni evaluación de módulos, no cuenta como RA.
- La app móvil de relleno: que tenga sentido offline y use algo del dispositivo (cámara, GPS, sensores, notificaciones).
- Empezar por la interfaz y dejar la infraestructura (SI/seguridad) para el final: el despliegue documentado es medio proyecto.
- No versionar desde el día 1: el historial de Git es una prueba más del trabajo.

---

¿Quieres que desarrolle una de estas ideas en profundidad (análisis de requisitos, modelo de datos, 
arquitectura, protocolo de red y planificación)? Dime cuál y la convierto en el documento base del proyecto.
