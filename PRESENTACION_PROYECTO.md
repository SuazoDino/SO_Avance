# 📋 PRESENTACIÓN DEL PROYECTO
## Simulador de Sistema Operativo - Gestión de Memoria y Procesos

---

## 1. EXPLICACIÓN DE LA ARQUITECTURA ASUMIDA

### 1.1 Tecnología Base
- **Lenguaje de programación**: Python 3
- **Framework gráfico**: Tkinter (interfaz de usuario)
- **Paradigma**: Programación orientada a objetos (POO)
- **Arquitectura**: Modular y desacoplada

### 1.2 Arquitectura General del Sistema

El sistema está estructurado en **8 módulos independientes** que se comunican entre sí a través de un coordinador central:

#### **Estructura Modular:**
- **`main.py`**: Punto de entrada del programa
- **`interfaz.py`**: Módulo de interfaz gráfica (presentación)
- **`coordinador.py`**: Coordinador central que integra todos los módulos
- **`modulo_cpu.py`**: Gestión de la unidad de procesamiento
- **`modulo_procesos.py`**: Gestión de procesos y sus estados
- **`modulo_memoria.py`**: Gestión de asignación de memoria
- **`modulo_planificador.py`**: Selección de procesos a ejecutar
- **`modulo_despachador.py`**: Asignación de CPU a procesos
- **`constantes.py`**: Configuraciones y constantes del sistema

### 1.3 Comunicación Interna y Flujo de Datos

**Patrón de diseño**: **Coordinador Central (Mediator Pattern)**

- El **CoordinadorSO** actúa como mediador entre todos los módulos
- Cada módulo tiene responsabilidades específicas y bien definidas
- La comunicación se realiza a través del coordinador, evitando dependencias directas entre módulos
- El flujo de datos es unidireccional y controlado

**Flujo de ejecución en cada ciclo (tick):**
1. **Coordinador** recibe solicitud de ejecución
2. **Gestor de Procesos** → Carga procesos nuevos a memoria
3. **Gestor de Memoria** → Asigna espacio disponible
4. **Gestor de Procesos** → Maneja retorno de procesos bloqueados (I/O)
5. **CPU** → Ejecuta un tick del proceso actual
6. **Planificador** → Selecciona próximo proceso según algoritmo
7. **Despachador** → Asigna CPU al proceso seleccionado
8. **Interfaz** → Actualiza visualización en tiempo real

### 1.4 Interacción entre Componentes

**Jerarquía de dependencias:**
```
main.py
  └── interfaz.py
        └── coordinador.py
              ├── modulo_cpu.py
              ├── modulo_procesos.py
              ├── modulo_memoria.py
              ├── modulo_planificador.py
              └── modulo_despachador.py
                    └── constantes.py
```

**Principios de diseño aplicados:**
- **Separación de responsabilidades**: Cada módulo tiene una función única
- **Bajo acoplamiento**: Los módulos no dependen directamente entre sí
- **Alta cohesión**: Cada módulo agrupa funcionalidades relacionadas
- **Reutilización**: Los módulos pueden modificarse sin afectar otros

---

## 2. REQUERIMIENTOS ATENDIDOS

### 2.1 Gestión de Procesos
- ✅ **Creación de procesos**: Permite crear procesos con tamaño, tiempo de ejecución y prioridad
- ✅ **Estados de proceso**: Implementa los 5 estados clásicos (NUEVO, LISTO, EJECUCION, BLOQUEADO, TERMINADO)
- ✅ **Colas de procesos**: Gestiona colas separadas para cada estado
- ✅ **PCB (Process Control Block)**: Almacena toda la información de cada proceso
- ✅ **Transiciones de estado**: Maneja automáticamente los cambios entre estados

### 2.2 Gestión de Memoria
- ✅ **Asignación dinámica**: Asigna memoria a procesos según su tamaño
- ✅ **Algoritmos de asignación**: Implementa 3 estrategias:
  - **First Fit**: Primer bloque disponible que cumpla
  - **Best Fit**: Bloque más pequeño que cumpla
  - **Worst Fit**: Bloque más grande disponible
- ✅ **Liberación de memoria**: Libera automáticamente cuando un proceso termina
- ✅ **Compactación**: Une bloques libres adyacentes automáticamente
- ✅ **Visualización**: Muestra el mapa de memoria en tiempo real
- ✅ **Configuración de tamaño**: Permite cambiar el tamaño total de memoria

### 2.3 Planificación de Procesos
- ✅ **Múltiples algoritmos**: Implementa 4 algoritmos de planificación:
  - **Round Robin**: Con quantum configurable
  - **FCFS** (First Come First Served): FIFO simple
  - **SJF** (Shortest Job First): Por tiempo de ejecución
  - **Prioridad**: Por nivel de prioridad
- ✅ **Cambio dinámico**: Permite cambiar el algoritmo durante la ejecución
- ✅ **Quantum configurable**: Ajuste del quantum para Round Robin
- ✅ **Gráfico de Gantt**: Visualización de la línea de tiempo de ejecución

### 2.4 Gestión de CPU
- ✅ **Ejecución por ticks**: Simula unidades de tiempo discretas
- ✅ **Manejo de quantum**: Controla el agotamiento del quantum en Round Robin
- ✅ **Bloqueos por I/O**: Simula bloqueos aleatorios de procesos
- ✅ **Retorno de I/O**: Maneja el retorno de procesos bloqueados

### 2.5 Interfaz de Usuario
- ✅ **Panel de configuración**: Permite ajustar parámetros del sistema
- ✅ **Tabla de procesos**: Muestra estado actual de todos los procesos
- ✅ **Visualización de memoria**: Representación gráfica del mapa de memoria
- ✅ **Gráfico de Gantt**: Línea de tiempo de uso de CPU
- ✅ **Log de eventos**: Registro en tiempo real de todas las operaciones
- ✅ **Agregar procesos manualmente**: Creación de procesos personalizados
- ✅ **Generación automática**: Crea procesos de prueba predefinidos
- ✅ **Control de simulación**: Iniciar, pausar y reiniciar la simulación
- ✅ **Tema visual moderno**: Interfaz con tema oscuro futurista
- ✅ **Hover informativo**: Información detallada al pasar el mouse sobre memoria
- ✅ **Actualización en tiempo real**: Interfaz se actualiza cada 200ms durante la simulación

### 2.6 Funcionalidades Adicionales
- ✅ **Colores por proceso**: Cada proceso tiene un color único para identificación
- ✅ **Reinicio del sistema**: Capacidad de reiniciar completamente el simulador
- ✅ **Manejo de errores**: Validación de entradas y mensajes informativos
- ✅ **Interfaz responsiva**: Componentes que se adaptan al contenido

---

## 3. DESARROLLO DE LA INTERFAZ GRÁFICA

### 3.1 Arquitectura de la Interfaz

La interfaz gráfica del simulador está implementada utilizando **Tkinter** con un enfoque orientado a objetos. La clase principal `SimuladorApp` gestiona todos los componentes visuales y la comunicación con el coordinador del sistema operativo.

**Estructura de la Interfaz:**
- **Ventana principal**: 1400x950 píxeles con tema oscuro futurista
- **Layout modular**: Componentes organizados en paneles independientes
- **Actualización dinámica**: Bucle de simulación que actualiza la UI cada 200ms
- **Comunicación bidireccional**: La interfaz envía comandos y recibe actualizaciones del coordinador

### 3.2 Componentes Principales

#### **3.2.1 Panel de Configuración**
Ubicado en el lado izquierdo de la ventana, permite configurar todos los parámetros del sistema:

- **Configuración de Memoria**:
  - Campo para establecer el tamaño total de RAM (en KB)
  - Botón para aplicar cambios (reinicia el sistema)
  - Validación de entrada para valores positivos

- **Algoritmo de Planificación**:
  - ComboBox con 4 opciones: Round Robin, FCFS, SJF, Prioridad
  - Cambio dinámico durante la ejecución
  - Habilitación/deshabilitación automática del campo quantum según el algoritmo

- **Configuración de Quantum**:
  - Campo numérico para establecer el quantum (solo para Round Robin)
  - Botón de confirmación para aplicar cambios
  - Se deshabilita automáticamente para algoritmos que no lo requieren

- **Estrategia de Asignación de Memoria**:
  - ComboBox con 3 opciones: First Fit, Best Fit, Worst Fit
  - Cambio dinámico que afecta la asignación de nuevos procesos

- **Botones de Acción**:
  - **Agregar Proceso Manual**: Abre ventana modal para crear procesos personalizados
  - **Generar Test Automático**: Crea 4 procesos de prueba predefinidos
  - **Iniciar/Pausar Simulación**: Control principal de la ejecución

#### **3.2.2 Tabla de Procesos**
Muestra el estado actual de todos los procesos en el sistema:

- **Columnas**:
  - PID: Identificador único del proceso
  - Estado: Estado actual con iconos visuales (🆕 NUEVO, ✅ LISTO, ⚡ EJECUCION, ⏸️ BLOQUEADO, ✔️ TERMINADO)
  - Burst: Tiempo de ejecución restante
  - Size: Tamaño del proceso en KB
  - Prio: Prioridad del proceso

- **Características**:
  - Actualización en tiempo real durante la simulación
  - Ordenamiento automático por PID
  - Scrollbar para manejar muchos procesos
  - Resaltado visual del proceso en ejecución

#### **3.2.3 Visualización de Memoria**
Representación gráfica del mapa de memoria:

- **Representación Visual**:
  - Cada bloque de memoria se muestra como un rectángulo proporcional
  - Bloques ocupados tienen colores únicos por proceso
  - Bloques libres se muestran en gris
  - El proceso en ejecución se resalta con color dorado y borde brillante
  - Etiquetas muestran PID y tamaño de cada bloque

- **Funcionalidad de Hover**:
  - Al pasar el mouse sobre un bloque, se muestra información detallada:
    - Estado (LIBRE, OCUPADO, EJECUTANDO)
    - PID del proceso (si está ocupado)
    - Tamaño del bloque en KB
    - Dirección de inicio en memoria
  - El label inferior muestra esta información en tiempo real

- **Características Técnicas**:
  - Escalado automático según el tamaño total de memoria
  - Actualización dinámica cuando cambia el tamaño de memoria
  - Visualización de direcciones de memoria en el lado izquierdo

#### **3.2.4 Gráfico de Gantt**
Línea de tiempo que muestra el historial de uso de CPU:

- **Visualización**:
  - Cada segmento representa un período de ejecución de un proceso
  - Colores corresponden a los procesos (mismo color que en memoria)
  - El proceso actual se resalta con color dorado
  - Muestra los últimos 60 ticks de ejecución

- **Características**:
  - Escalado automático según el ancho disponible
  - Etiquetas con PID en segmentos grandes
  - Botón para limpiar el historial
  - Actualización continua durante la simulación

#### **3.2.5 Log de Eventos**
Registro textual de todas las operaciones del sistema:

- **Funcionalidades**:
  - Muestra todos los eventos con timestamp (HH:MM:SS)
  - Scroll automático al final del log
  - Límite de 200 líneas (elimina las más antiguas automáticamente)
  - Fuente monospace (Consolas) para mejor legibilidad
  - Scrollbar vertical para navegar el historial

- **Tipos de Eventos Registrados**:
  - Carga de procesos a memoria
  - Cambios de estado de procesos
  - Asignación y liberación de memoria
  - Cambios de algoritmo de planificación
  - Terminación de procesos
  - Bloqueos y retornos de I/O
  - Reinicios del sistema

### 3.3 Ventana de Agregar Proceso Manual

Ventana modal que permite crear procesos personalizados:

- **Campos de Entrada**:
  - **Tamaño (KB)**: Tamaño del proceso en kilobytes
  - **Tiempo de Ejecución (Seg)**: Duración total del proceso
  - **Prioridad**: Nivel de prioridad (número entero)

- **Validación**:
  - Verifica que todos los valores sean numéricos
  - Valida que los valores sean mayores a 0
  - Muestra mensaje de confirmación antes de crear

- **Diseño**:
  - Ventana modal no redimensionable (380x400)
  - Tema consistente con la ventana principal
  - Botones de confirmar y cancelar

### 3.4 Sistema de Estilos y Temas

La interfaz utiliza un **tema oscuro futurista** con los siguientes elementos:

- **Colores Principales**:
  - Fondo principal: Tonos oscuros (#1a2332, #2a3441)
  - Texto: Blanco y dorado para resaltar
  - Proceso en ejecución: Dorado brillante (#FFD700)
  - Bordes: Dorado para elementos importantes

- **Estilos Tkinter**:
  - Configuración personalizada de ttk.Style
  - Estilos para botones, labels, combobox, treeview
  - Efectos hover en botones
  - Botones de acción con estilo especial (Action.TButton)

- **Tipografía**:
  - Segoe UI para texto general
  - Consolas para el log (monospace)
  - Tamaños variables según importancia

### 3.5 Flujo de Actualización

El sistema utiliza un bucle de simulación asíncrono:

1. **Usuario inicia simulación** → `toggle()` cambia el estado
2. **Bucle principal** → `loop()` se ejecuta cada 200ms:
   - Llama a `coordinador.ejecutar_ciclo()` para ejecutar un tick
   - Recibe mensajes de log y los muestra
   - Actualiza la tabla de procesos (`update_ui()`)
   - Redibuja la memoria (`draw_mem()`)
   - Redibuja el gráfico de Gantt (`draw_gantt()`)
   - Programa la siguiente iteración con `root.after(200, self.loop)`

3. **Actualización de Componentes**:
   - Tabla: Se limpia y se vuelve a poblar con procesos actuales
   - Memoria: Se recalcula el mapa y se redibuja completamente
   - Gantt: Se actualiza con los últimos 60 ticks
   - Log: Se agregan nuevos mensajes al final

### 3.6 Funcionalidades Interactivas

- **Cambio Dinámico de Configuración**:
  - Los cambios en algoritmo, quantum y estrategia de memoria se aplican inmediatamente
  - El cambio de tamaño de memoria reinicia todo el sistema
  - Los procesos existentes se mantienen al cambiar algoritmos

- **Generación de Test Automático**:
  - Crea 4 procesos predefinidos con diferentes características:
    - Proceso 1: 100 KB, 20 seg, prioridad 5
    - Proceso 2: 100 KB, 5 seg, prioridad 1
    - Proceso 3: 100 KB, 10 seg, prioridad 3
    - Proceso 4: 100 KB, 2 seg, prioridad 4

- **Control de Simulación**:
  - Botón que alterna entre "INICIAR" y "PAUSAR"
  - Al pausar, el sistema mantiene su estado actual
  - Al reiniciar, continúa desde donde se pausó

### 3.7 Integración con el Coordinador

La interfaz actúa como capa de presentación sobre el coordinador:

- **Comunicación**:
  - La interfaz envía comandos al coordinador (agregar proceso, cambiar configuración)
  - El coordinador ejecuta la lógica y retorna mensajes de log
  - La interfaz consulta el estado actual para actualizar visualizaciones

- **Métodos de Interacción**:
  - `coordinador.agregar_proceso()`: Crea nuevos procesos
  - `coordinador.ejecutar_ciclo()`: Ejecuta un ciclo de simulación
  - `coordinador.cambiar_algoritmo()`: Cambia el algoritmo de planificación
  - `coordinador.cambiar_quantum()`: Ajusta el quantum
  - `coordinador.cambiar_estrategia_memoria()`: Cambia la estrategia de memoria
  - `coordinador.reiniciar_memoria()`: Reinicia el sistema con nuevo tamaño

### 3.8 Avances y Características Destacadas

**Avances Implementados:**
- ✅ Interfaz gráfica completa y funcional
- ✅ Visualización en tiempo real de todos los componentes
- ✅ Tema visual moderno y profesional
- ✅ Interactividad completa con el usuario
- ✅ Validación de entradas y manejo de errores
- ✅ Ventanas modales para operaciones específicas
- ✅ Sistema de log completo para seguimiento
- ✅ Hover informativo en visualización de memoria
- ✅ Gráfico de Gantt dinámico
- ✅ Control total de la simulación

**Mejoras de Usabilidad:**
- Iconos visuales para estados de procesos
- Colores únicos por proceso para fácil identificación
- Resaltado del proceso en ejecución en múltiples componentes
- Información contextual al pasar el mouse
- Mensajes de confirmación para operaciones importantes
- Scroll automático en el log de eventos

---

## 4. DEMOSTRACIÓN DEL MÓDULO DESARROLLADO

### 4.1 Módulo Principal: Simulador Completo de Sistema Operativo

**Descripción general:**
Se desarrolló un **simulador completo de sistema operativo** que integra todos los componentes esenciales: gestión de procesos, gestión de memoria, planificación de CPU y visualización en tiempo real.

### 4.2 Funcionamiento del Sistema

#### **Entradas:**
- **Configuración inicial**:
  - Tamaño total de memoria (en KB)
  - Algoritmo de planificación seleccionado
  - Tamaño del quantum (para Round Robin)
  - Estrategia de asignación de memoria

- **Procesos a simular**:
  - Tamaño del proceso (KB)
  - Tiempo de ejecución (ticks/segundos)
  - Prioridad (número entero)

#### **Procesos internos:**
1. **Carga de procesos**: Los procesos nuevos intentan cargarse a memoria
2. **Asignación de memoria**: Se busca espacio disponible según la estrategia configurada
3. **Cola de listos**: Procesos con memoria asignada esperan ejecución
4. **Planificación**: El planificador selecciona el próximo proceso según el algoritmo
5. **Despacho**: El despachador asigna la CPU al proceso seleccionado
6. **Ejecución**: La CPU ejecuta un tick del proceso actual
7. **Transiciones**: El proceso puede terminar, bloquearse por I/O, o agotar su quantum
8. **Liberación**: Al terminar, se libera la memoria y se actualiza el estado

#### **Salidas:**
- **Visualización en tiempo real**:
  - Tabla de procesos con estados actualizados
  - Mapa de memoria mostrando bloques ocupados/libres
  - Gráfico de Gantt con historial de ejecución
  - Log de eventos con todas las operaciones

- **Información detallada**:
  - Estado de cada proceso (NUEVO, LISTO, EJECUCION, BLOQUEADO, TERMINADO)
  - Ubicación en memoria de cada proceso
  - Tiempo restante de ejecución
  - Prioridad y tamaño de cada proceso

### 4.3 Comportamiento Esperado

**Ciclo de vida de un proceso:**
1. **Creación**: El proceso se crea y entra en estado NUEVO
2. **Carga a memoria**: Si hay espacio, se asigna memoria y pasa a LISTO
3. **Selección**: El planificador lo selecciona según el algoritmo
4. **Ejecución**: El despachador le asigna CPU, pasa a EJECUCION
5. **Transiciones posibles**:
   - **Terminación**: Si completa su tiempo de ejecución → TERMINADO
   - **Bloqueo**: Si requiere I/O → BLOQUEADO (luego retorna a LISTO)
   - **Quantum agotado**: En Round Robin → vuelve a LISTO
6. **Liberación**: Al terminar, se libera su memoria

**Comportamiento del sistema:**
- Ejecuta ciclos continuos mientras la simulación está activa
- Actualiza la interfaz cada 200ms (5 veces por segundo)
- Maneja múltiples procesos simultáneamente
- Gestiona fragmentación de memoria automáticamente
- Registra todos los eventos para análisis posterior

### 4.4 Pasos para la Demostración

#### **Paso 1: Inicio del Sistema**
- Ejecutar `python main.py`
- Mostrar la interfaz inicial con memoria vacía
- Explicar los paneles disponibles

#### **Paso 2: Configuración**
- Configurar tamaño de memoria (ej: 1024 KB)
- Seleccionar algoritmo de planificación (ej: Round Robin)
- Ajustar quantum si es necesario (ej: 3 ticks)
- Seleccionar estrategia de memoria (ej: First Fit)

#### **Paso 3: Creación de Procesos**
- **Opción A**: Agregar proceso manualmente
  - Mostrar ventana de creación
  - Ingresar: tamaño (100 KB), tiempo (10 seg), prioridad (1)
  - Confirmar y observar cómo aparece en la tabla
  
- **Opción B**: Generar test automático
  - Presionar "Generar Test Automático"
  - Observar cómo se crean 4 procesos de prueba

#### **Paso 4: Iniciar Simulación**
- Presionar "INICIAR SIMULACIÓN"
- Observar cómo los procesos se cargan a memoria
- Ver cómo cambian de estado en la tabla
- Mostrar la visualización de memoria llenándose

#### **Paso 5: Observar Ejecución**
- **Memoria**: Mostrar cómo se asignan bloques de diferentes colores
- **Tabla de procesos**: Ver cambios de estado en tiempo real
- **Gráfico de Gantt**: Observar la línea de tiempo de ejecución
- **Log de eventos**: Leer los mensajes de cada acción

#### **Paso 6: Cambiar Algoritmo en Tiempo Real**
- Cambiar de Round Robin a SJF
- Observar cómo cambia el orden de ejecución
- Explicar la diferencia en el comportamiento

#### **Paso 7: Proceso en Ejecución**
- Identificar el proceso en ejecución (color dorado en memoria)
- Mostrar el icono ⚡ en la tabla
- Explicar el cambio de contexto

#### **Paso 8: Terminación de Procesos**
- Observar cuando un proceso termina
- Ver cómo se libera su memoria (bloque se vuelve libre)
- Confirmar en el log el mensaje de terminación

#### **Paso 9: Bloqueos por I/O**
- Esperar a que un proceso se bloquee (en FCFS/SJF/Prioridad)
- Mostrar cómo pasa a estado BLOQUEADO
- Observar su retorno automático después de unos ticks

#### **Paso 10: Cambiar Estrategia de Memoria**
- Cambiar de First Fit a Best Fit
- Agregar nuevos procesos
- Explicar la diferencia en la asignación

#### **Paso 11: Reiniciar Sistema**
- Cambiar tamaño de memoria
- Observar cómo se reinicia todo
- Confirmar que todos los procesos se eliminan

#### **Paso 12: Hover en Memoria**
- Pasar el mouse sobre bloques de memoria
- Mostrar información detallada (PID, tamaño, dirección)
- Explicar la utilidad para análisis

---

## 5. RESUMEN EJECUTIVO

### Características Destacadas:
- ✅ **Arquitectura modular** bien estructurada y mantenible
- ✅ **4 algoritmos de planificación** implementados y funcionales
- ✅ **3 estrategias de memoria** con visualización en tiempo real
- ✅ **Interfaz gráfica completa** con múltiples visualizaciones
- ✅ **Simulación en tiempo real** con control total del usuario
- ✅ **Documentación completa** de todos los módulos

### Valor del Proyecto:
Este simulador permite **comprender visualmente** cómo funcionan los componentes fundamentales de un sistema operativo, facilitando el aprendizaje de conceptos complejos como planificación de procesos, gestión de memoria y cambio de contexto.

---

**Fin del documento de presentación**

