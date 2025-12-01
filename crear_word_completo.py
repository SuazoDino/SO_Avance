#!/usr/bin/env python3
"""
Crea un documento Word COMPLETO y PROFESIONAL con todo el contenido detallado
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def agregar_portada(doc):
    """Crea una portada profesional"""
    # Título principal
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("SIMULADOR DE SISTEMA OPERATIVO")
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    doc.add_paragraph()
    
    # Subtítulo
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run("Gestión de Memoria y Procesos")
    run2.font.size = Pt(20)
    run2.font.color.rgb = RGBColor(102, 102, 102)
    
    doc.add_paragraph()
    doc.add_paragraph()
    
    # Información del proyecto
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run3 = p3.add_run("Documentación Técnica Completa")
    run3.font.size = Pt(14)
    run3.italic = True
    
    doc.add_page_break()

def crear_tabla_detallada(doc, titulo, encabezados, datos, estilo='Light Grid Accent 1'):
    """Crea una tabla detallada con formato"""
    doc.add_paragraph()
    p = doc.add_paragraph(titulo)
    p.runs[0].font.bold = True
    p.runs[0].font.size = Pt(12)
    doc.add_paragraph()
    
    tabla = doc.add_table(rows=1, cols=len(encabezados))
    tabla.style = estilo
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Encabezado
    hdr_cells = tabla.rows[0].cells
    for i, encabezado in enumerate(encabezados):
        hdr_cells[i].text = encabezado
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), '4472C4')
        hdr_cells[i]._element.get_or_add_tcPr().append(shading_elm)
    
    # Datos
    for fila in datos:
        row_cells = tabla.add_row().cells
        for i, valor in enumerate(fila):
            if i < len(row_cells):
                row_cells[i].text = str(valor)
                if i == 0:  # Primera columna en negrita
                    if len(row_cells[i].paragraphs[0].runs) > 0:
                        row_cells[i].paragraphs[0].runs[0].font.bold = True
                    else:
                        run = row_cells[i].paragraphs[0].add_run(str(valor))
                        run.font.bold = True
                        row_cells[i].text = str(valor)
    
    doc.add_paragraph()

def crear_documento_completo():
    """Crea documento Word completo y profesional"""
    doc = Document()
    
    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3)
        section.right_margin = Cm(3)
    
    # PORTADA
    agregar_portada(doc)
    
    # ÍNDICE
    doc.add_heading("ÍNDICE", 1)
    indice = [
        "1. EXPLICACIÓN DE LA ARQUITECTURA ASUMIDA",
        "2. REQUERIMIENTOS ATENDIDOS",
        "3. DESARROLLO DE LA INTERFAZ GRÁFICA",
        "4. DEMOSTRACIÓN DEL MÓDULO DESARROLLADO",
        "5. RESUMEN EJECUTIVO"
    ]
    for item in indice:
        p = doc.add_paragraph(item, style='List Number')
        p.runs[0].font.size = Pt(11)
    doc.add_page_break()
    
    # 1. ARQUITECTURA
    doc.add_heading("1. EXPLICACIÓN DE LA ARQUITECTURA ASUMIDA", 1)
    
    doc.add_heading("1.1 Tecnología Base", 2)
    crear_tabla_detallada(doc, "Especificaciones Técnicas:",
        ["Componente", "Tecnología Utilizada"],
        [
            ["Lenguaje de programación", "Python 3"],
            ["Framework gráfico", "Tkinter (interfaz de usuario)"],
            ["Paradigma", "Programación orientada a objetos (POO)"],
            ["Arquitectura", "Modular y desacoplada"],
            ["Patrón de diseño", "Coordinador Central (Mediator Pattern)"],
            ["Gestión de memoria", "Asignación dinámica con 3 algoritmos"],
            ["Planificación", "4 algoritmos implementados"]
        ])
    
    doc.add_heading("1.2 Arquitectura General del Sistema", 2)
    p = doc.add_paragraph()
    p.add_run("El sistema está estructurado en ").bold = False
    p.add_run("8 módulos independientes").bold = True
    p.add_run(" que se comunican entre sí a través de un coordinador central.").bold = False
    
    crear_tabla_detallada(doc, "Estructura Modular del Sistema:",
        ["Módulo", "Archivo", "Responsabilidad Principal"],
        [
            ["Interfaz Gráfica", "interfaz.py", "Visualización en tiempo real, panel de control, gráficos"],
            ["Coordinador", "coordinador.py", "Integración y coordinación de todos los módulos"],
            ["CPU", "modulo_cpu.py", "Ejecución de procesos por ticks, manejo de quantum"],
            ["Gestor de Procesos", "modulo_procesos.py", "Creación, estados y colas de procesos"],
            ["Gestor de Memoria", "modulo_memoria.py", "Asignación, liberación y compactación de memoria"],
            ["Planificador", "modulo_planificador.py", "Selección de procesos según algoritmo"],
            ["Despachador", "modulo_despachador.py", "Asignación de CPU y cambio de contexto"],
            ["Constantes", "constantes.py", "Configuraciones, colores y constantes del sistema"]
        ], 'Medium Grid 1 Accent 1')
    
    doc.add_heading("1.3 Flujo de Ejecución", 2)
    p = doc.add_paragraph("El sistema ejecuta ciclos continuos (ticks) con el siguiente flujo:")
    pasos = [
        "Coordinador recibe solicitud de ejecución",
        "Gestor de Procesos carga procesos nuevos a memoria",
        "Gestor de Memoria asigna espacio disponible según estrategia",
        "Gestor de Procesos maneja retorno de procesos bloqueados (I/O)",
        "CPU ejecuta un tick del proceso actual",
        "Planificador selecciona próximo proceso según algoritmo configurado",
        "Despachador asigna CPU al proceso seleccionado",
        "Interfaz actualiza visualización en tiempo real (cada 200ms)"
    ]
    for i, paso in enumerate(pasos, 1):
        p = doc.add_paragraph(f"{i}. {paso}", style='List Number')
    
    doc.add_page_break()
    
    # 2. REQUERIMIENTOS
    doc.add_heading("2. REQUERIMIENTOS ATENDIDOS", 1)
    
    doc.add_heading("2.1 Gestión de Procesos", 2)
    crear_tabla_detallada(doc, "Funcionalidades de Gestión de Procesos:",
        ["Funcionalidad", "Descripción", "Estado"],
        [
            ["Creación de procesos", "Permite crear procesos con tamaño, tiempo y prioridad", "✅ Implementado"],
            ["Estados de proceso", "5 estados: NUEVO, LISTO, EJECUCION, BLOQUEADO, TERMINADO", "✅ Implementado"],
            ["Colas de procesos", "Gestiona colas separadas para cada estado", "✅ Implementado"],
            ["PCB (Process Control Block)", "Almacena toda la información de cada proceso", "✅ Implementado"],
            ["Transiciones de estado", "Maneja automáticamente los cambios entre estados", "✅ Implementado"],
            ["Bloqueos por I/O", "Simula bloqueos aleatorios y retorno automático", "✅ Implementado"]
        ])
    
    doc.add_heading("2.2 Gestión de Memoria", 2)
    crear_tabla_detallada(doc, "Algoritmos de Asignación de Memoria:",
        ["Algoritmo", "Descripción", "Ventajas"],
        [
            ["First Fit", "Primer bloque disponible que cumpla con el tamaño", "Rápido, bajo overhead"],
            ["Best Fit", "Bloque más pequeño que cumpla con el tamaño", "Minimiza fragmentación interna"],
            ["Worst Fit", "Bloque más grande disponible", "Deja bloques grandes para futuros procesos"]
        ])
    
    p = doc.add_paragraph()
    p.add_run("Características adicionales: ").bold = True
    p.add_run("Asignación dinámica, liberación automática, compactación de bloques libres adyacentes, visualización en tiempo real, configuración de tamaño total de memoria.")
    
    doc.add_heading("2.3 Planificación de Procesos", 2)
    crear_tabla_detallada(doc, "Algoritmos de Planificación Implementados:",
        ["Algoritmo", "Tipo", "Características", "Uso Recomendado"],
        [
            ["Round Robin", "Con quantum", "Quantum configurable, cambio de contexto por tiempo", "Sistemas interactivos"],
            ["FCFS", "FIFO simple", "Sin preemption, orden de llegada", "Procesos batch cortos"],
            ["SJF", "Por tiempo", "Ordena por tiempo de ejecución restante", "Minimiza tiempo de espera"],
            ["Prioridad", "Por nivel", "Menor número = mayor prioridad, puede ser preemptivo", "Sistemas con prioridades"]
        ], 'Colorful Grid Accent 2')
    
    doc.add_heading("2.4 Estados de Proceso", 2)
    crear_tabla_detallada(doc, "Estados Implementados:",
        ["Estado", "Descripción", "Transiciones Posibles"],
        [
            ["NUEVO", "Proceso recién creado, esperando ser cargado a memoria", "→ LISTO (cuando hay memoria)"],
            ["LISTO", "Proceso en memoria, listo para ejecutarse, esperando CPU", "→ EJECUCION (cuando se asigna CPU)"],
            ["EJECUCION", "Proceso actualmente ejecutándose en la CPU", "→ LISTO, BLOQUEADO, TERMINADO"],
            ["BLOQUEADO", "Proceso esperando I/O o algún recurso", "→ LISTO (cuando termina I/O)"],
            ["TERMINADO", "Proceso que ha finalizado su ejecución", "Memoria liberada"]
        ])
    
    doc.add_page_break()
    
    # 3. INTERFAZ GRÁFICA
    doc.add_heading("3. DESARROLLO DE LA INTERFAZ GRÁFICA", 1)
    
    doc.add_heading("3.1 Arquitectura de la Interfaz", 2)
    p = doc.add_paragraph()
    p.add_run("La interfaz gráfica está implementada utilizando ").bold = False
    p.add_run("Tkinter").bold = True
    p.add_run(" con un enfoque orientado a objetos. La clase principal ").bold = False
    p.add_run("SimuladorApp").bold = True
    p.add_run(" gestiona todos los componentes visuales y la comunicación con el coordinador del sistema operativo.").bold = False
    
    crear_tabla_detallada(doc, "Características de la Interfaz:",
        ["Característica", "Especificación"],
        [
            ["Ventana principal", "1400x950 píxeles"],
            ["Tema visual", "Oscuro futurista con colores personalizados"],
            ["Layout", "Modular con paneles independientes"],
            ["Actualización", "Bucle de simulación cada 200ms (5 veces por segundo)"],
            ["Comunicación", "Bidireccional: envía comandos y recibe actualizaciones"],
            ["Responsividad", "Componentes que se adaptan al contenido"]
        ])
    
    doc.add_heading("3.2 Componentes Principales de la Interfaz", 2)
    
    doc.add_heading("3.2.1 Panel de Configuración", 3)
    crear_tabla_detallada(doc, "Elementos del Panel de Configuración:",
        ["Elemento", "Funcionalidad"],
        [
            ["Configuración de Memoria", "Campo para establecer tamaño total de RAM (KB), botón para aplicar cambios"],
            ["Algoritmo de Planificación", "ComboBox con 4 opciones: Round Robin, FCFS, SJF, Prioridad"],
            ["Configuración de Quantum", "Campo numérico para Round Robin, se deshabilita para otros algoritmos"],
            ["Estrategia de Memoria", "ComboBox: First Fit, Best Fit, Worst Fit"],
            ["Agregar Proceso Manual", "Botón que abre ventana modal para crear procesos personalizados"],
            ["Generar Test Automático", "Crea 4 procesos de prueba predefinidos"],
            ["Iniciar/Pausar Simulación", "Control principal de la ejecución"]
        ])
    
    doc.add_heading("3.2.2 Tabla de Procesos", 3)
    crear_tabla_detallada(doc, "Columnas y Funcionalidades:",
        ["Columna", "Descripción"],
        [
            ["PID", "Identificador único del proceso"],
            ["Estado", "Estado actual con iconos visuales (🆕 NUEVO, ✅ LISTO, ⚡ EJECUCION, ⏸️ BLOQUEADO, ✔️ TERMINADO)"],
            ["Burst", "Tiempo de ejecución restante"],
            ["Size", "Tamaño del proceso en KB"],
            ["Prio", "Prioridad del proceso"]
        ])
    p = doc.add_paragraph()
    p.add_run("Características: ").bold = True
    p.add_run("Actualización en tiempo real, ordenamiento automático por PID, scrollbar para muchos procesos, resaltado visual del proceso en ejecución.")
    
    doc.add_heading("3.2.3 Visualización de Memoria", 3)
    p = doc.add_paragraph("Representación gráfica del mapa de memoria con las siguientes características:")
    caracteristicas_mem = [
        "Cada bloque de memoria se muestra como un rectángulo proporcional",
        "Bloques ocupados tienen colores únicos por proceso para fácil identificación",
        "Bloques libres se muestran en gris",
        "El proceso en ejecución se resalta con color dorado y borde brillante",
        "Etiquetas muestran PID y tamaño de cada bloque",
        "Hover informativo: al pasar el mouse muestra estado, PID, tamaño y dirección",
        "Escalado automático según el tamaño total de memoria",
        "Visualización de direcciones de memoria en el lado izquierdo"
    ]
    for item in caracteristicas_mem:
        doc.add_paragraph(item, style='List Bullet')
    
    doc.add_heading("3.2.4 Gráfico de Gantt", 3)
    crear_tabla_detallada(doc, "Características del Gráfico de Gantt:",
        ["Característica", "Descripción"],
        [
            ["Visualización", "Línea de tiempo que muestra historial de uso de CPU"],
            ["Segmentos", "Cada segmento representa un período de ejecución de un proceso"],
            ["Colores", "Corresponden a los procesos (mismo color que en memoria)"],
            ["Resaltado", "El proceso actual se resalta con color dorado"],
            ["Historial", "Muestra los últimos 60 ticks de ejecución"],
            ["Escalado", "Automático según el ancho disponible"],
            ["Etiquetas", "Muestra PID en segmentos grandes"],
            ["Control", "Botón para limpiar el historial"]
        ])
    
    doc.add_heading("3.2.5 Log de Eventos", 3)
    crear_tabla_detallada(doc, "Funcionalidades del Log:",
        ["Funcionalidad", "Descripción"],
        [
            ["Timestamps", "Muestra todos los eventos con hora (HH:MM:SS)"],
            ["Scroll automático", "Se desplaza automáticamente al final del log"],
            ["Límite de líneas", "200 líneas máximo (elimina las más antiguas automáticamente)"],
            ["Fuente", "Monospace (Consolas) para mejor legibilidad"],
            ["Navegación", "Scrollbar vertical para navegar el historial"],
            ["Tipos de eventos", "Carga de procesos, cambios de estado, asignación/liberación de memoria, cambios de algoritmo, terminación, bloqueos I/O, reinicios"]
        ])
    
    doc.add_heading("3.3 Ventana de Agregar Proceso Manual", 2)
    crear_tabla_detallada(doc, "Campos de la Ventana:",
        ["Campo", "Tipo", "Descripción"],
        [
            ["Tamaño (KB)", "Numérico", "Tamaño del proceso en kilobytes"],
            ["Tiempo de Ejecución (Seg)", "Numérico", "Duración total del proceso"],
            ["Prioridad", "Numérico", "Nivel de prioridad (número entero)"]
        ])
    p = doc.add_paragraph()
    p.add_run("Validación: ").bold = True
    p.add_run("Verifica valores numéricos, valida que sean mayores a 0, muestra mensaje de confirmación antes de crear.")
    
    doc.add_heading("3.4 Sistema de Estilos y Temas", 2)
    crear_tabla_detallada(doc, "Paleta de Colores:",
        ["Elemento", "Color", "Código"],
        [
            ["Fondo principal", "Tonos oscuros", "#1a2332, #2a3441"],
            ["Texto", "Blanco y dorado", "RGB(255,255,255), RGB(255,215,0)"],
            ["Proceso en ejecución", "Dorado brillante", "#FFD700"],
            ["Bordes importantes", "Dorado", "RGB(255,215,0)"]
        ])
    
    doc.add_page_break()
    
    # 4. DEMOSTRACIÓN
    doc.add_heading("4. DEMOSTRACIÓN DEL MÓDULO DESARROLLADO", 1)
    
    doc.add_heading("4.1 Funcionamiento del Sistema", 2)
    doc.add_paragraph("El simulador ejecuta ciclos continuos mientras la simulación está activa. A continuación se detalla el proceso completo:")
    
    doc.add_heading("4.2 Ciclo de Vida de un Proceso", 2)
    pasos_proceso = [
        "Creación: El proceso se crea y entra en estado NUEVO",
        "Carga a memoria: Si hay espacio disponible, se asigna memoria y pasa a LISTO",
        "Selección: El planificador lo selecciona según el algoritmo configurado",
        "Ejecución: El despachador le asigna CPU, pasa a EJECUCION",
        "Transiciones: El proceso puede terminar, bloquearse por I/O, o agotar su quantum",
        "Liberación: Al terminar, se libera su memoria y se actualiza el estado"
    ]
    for paso in pasos_proceso:
        doc.add_paragraph(paso, style='List Bullet')
    
    doc.add_heading("4.3 Pasos para la Demostración", 2)
    pasos_demo = [
        "Inicio del Sistema: Ejecutar python main.py, mostrar interfaz inicial",
        "Configuración: Configurar tamaño de memoria, algoritmo, quantum, estrategia",
        "Creación de Procesos: Agregar manualmente o generar test automático",
        "Iniciar Simulación: Presionar INICIAR, observar carga a memoria",
        "Observar Ejecución: Ver cambios en memoria, tabla, Gantt y log",
        "Cambiar Algoritmo: Cambiar en tiempo real y observar diferencias",
        "Proceso en Ejecución: Identificar proceso dorado en memoria",
        "Terminación: Observar liberación de memoria al terminar procesos",
        "Bloqueos I/O: Esperar bloqueos y retorno automático",
        "Cambiar Estrategia: Cambiar estrategia de memoria y agregar procesos",
        "Reiniciar Sistema: Cambiar tamaño de memoria y observar reinicio",
        "Hover en Memoria: Pasar mouse y ver información detallada"
    ]
    for i, paso in enumerate(pasos_demo, 1):
        p = doc.add_paragraph(f"{i}. {paso}", style='List Number')
    
    doc.add_page_break()
    
    # 5. RESUMEN
    doc.add_heading("5. RESUMEN EJECUTIVO", 1)
    
    doc.add_heading("5.1 Características Destacadas", 2)
    caracteristicas = [
        "Arquitectura modular bien estructurada y mantenible",
        "4 algoritmos de planificación implementados y funcionales",
        "3 estrategias de memoria con visualización en tiempo real",
        "Interfaz gráfica completa con múltiples visualizaciones",
        "Simulación en tiempo real con control total del usuario",
        "Documentación completa de todos los módulos",
        "Tema visual moderno y profesional",
        "Sistema de log completo para seguimiento",
        "Hover informativo en visualización de memoria",
        "Gráfico de Gantt dinámico"
    ]
    for caracteristica in caracteristicas:
        p = doc.add_paragraph(caracteristica, style='List Bullet')
        p.runs[0].font.size = Pt(11)
    
    doc.add_heading("5.2 Valor del Proyecto", 2)
    p = doc.add_paragraph()
    p.add_run("Este simulador permite ").bold = False
    p.add_run("comprender visualmente").bold = True
    p.add_run(" cómo funcionan los componentes fundamentales de un sistema operativo, facilitando el aprendizaje de conceptos complejos como planificación de procesos, gestión de memoria y cambio de contexto.").bold = False
    
    # Guardar
    doc.save('PRESENTACION_PROYECTO.docx')
    print("✅ Documento Word COMPLETO creado: PRESENTACION_PROYECTO.docx")
    print(f"   - Párrafos: {len(doc.paragraphs)}")
    print(f"   - Tablas: {len(doc.tables)}")
    print("   - Formato profesional con colores y estilos")
    print("   - Contenido detallado y completo")

if __name__ == '__main__':
    crear_documento_completo()
