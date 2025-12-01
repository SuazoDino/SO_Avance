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

### 2.6 Funcionalidades Adicionales
- ✅ **Tema visual moderno**: Interfaz con tema oscuro futurista
- ✅ **Colores por proceso**: Cada proceso tiene un color único para identificación
- ✅ **Hover informativo**: Información detallada al pasar el mouse sobre memoria
- ✅ **Reinicio del sistema**: Capacidad de reiniciar completamente el simulador

---

## 3. DEMOSTRACIÓN DEL MÓDULO DESARROLLADO

### 3.1 Módulo Principal: Simulador Completo de Sistema Operativo

**Descripción general:**
Se desarrolló un **simulador completo de sistema operativo** que integra todos los componentes esenciales: gestión de procesos, gestión de memoria, planificación de CPU y visualización en tiempo real.

### 3.2 Funcionamiento del Sistema

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

### 3.3 Comportamiento Esperado

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

### 3.4 Pasos para la Demostración

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

## 4. RESUMEN EJECUTIVO

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

