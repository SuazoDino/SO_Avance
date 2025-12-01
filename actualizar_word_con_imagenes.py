#!/usr/bin/env python3
"""
Actualiza el documento Word agregando imágenes en la sección de interfaz
y eliminando la sección 7 de imágenes requeridas
"""

from docx import Document
from docx.shared import Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
import glob

def agregar_imagen(doc, ruta_imagen, ancho=None, titulo=None):
    """Agrega una imagen al documento"""
    if os.path.exists(ruta_imagen):
        if titulo:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(titulo)
            run.bold = True
            run.font.size = Inches(0.15)
            doc.add_paragraph()
        
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        
        if ancho:
            run.add_picture(ruta_imagen, width=ancho)
        else:
            run.add_picture(ruta_imagen, width=Inches(6))
        
        doc.add_paragraph()
        return True
    return False

def actualizar_seccion_interfaz(doc):
    """Actualiza la sección 3 de interfaz agregando las imágenes"""
    
    # Buscar dónde está la sección 3
    imagenes_path = "Imagenes/"
    imagenes = sorted(glob.glob(os.path.join(imagenes_path, "*.png")))
    
    if not imagenes:
        print("⚠️ No se encontraron imágenes en la carpeta Imagenes/")
        return
    
    print(f"📸 Encontradas {len(imagenes)} imágenes")
    
    # Buscar la sección 3.2 Componentes Principales
    # Vamos a reemplazar/mejorar esa sección con imágenes
    
    # Primero, necesitamos encontrar dónde insertar las imágenes
    # Por ahora, agregaremos las imágenes después de cada subsección
    
    # Agregar imagen de interfaz completa al inicio de la sección 3.2
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.add_run("A continuación se muestran capturas de pantalla de la interfaz del simulador:").bold = True
    doc.add_paragraph()
    
    # Imagen 1: Interfaz completa (si existe)
    if len(imagenes) > 0:
        agregar_imagen(doc, imagenes[0], ancho=Inches(7), 
                      titulo="Figura 1: Vista completa de la interfaz del simulador")
    
    # Agregar imágenes en las subsecciones correspondientes
    # Imagen 2: Panel de configuración
    if len(imagenes) > 1:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run("Panel de Configuración:").bold = True
        agregar_imagen(doc, imagenes[1], ancho=Inches(5),
                      titulo="Figura 2: Panel de configuración con todos los controles")
    
    # Imagen 3: Tabla de procesos
    if len(imagenes) > 2:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run("Tabla de Procesos:").bold = True
        agregar_imagen(doc, imagenes[2], ancho=Inches(6),
                      titulo="Figura 3: Tabla de procesos mostrando diferentes estados")
    
    # Imagen 4: Memoria
    if len(imagenes) > 3:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run("Visualización de Memoria:").bold = True
        agregar_imagen(doc, imagenes[3], ancho=Inches(5),
                      titulo="Figura 4: Visualización gráfica del mapa de memoria")
    
    # Imagen 5: Gantt
    if len(imagenes) > 4:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run("Gráfico de Gantt:").bold = True
        agregar_imagen(doc, imagenes[4], ancho=Inches(6),
                      titulo="Figura 5: Gráfico de Gantt mostrando historial de ejecución")
    
    # Imagen 6: Log o proceso ejecutando
    if len(imagenes) > 5:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.add_run("Log de Eventos / Proceso en Ejecución:").bold = True
        agregar_imagen(doc, imagenes[5], ancho=Inches(6),
                      titulo="Figura 6: Log de eventos y proceso en ejecución")

def eliminar_seccion_7(doc):
    """Elimina la sección 7 de imágenes requeridas"""
    # Buscar y eliminar párrafos que contengan "7. IMÁGENES"
    para_eliminar = []
    en_seccion_7 = False
    
    for i, para in enumerate(doc.paragraphs):
        texto = para.text.strip()
        if "7. IMÁGENES" in texto.upper() or "7.1" in texto or "7.2" in texto:
            en_seccion_7 = True
        if en_seccion_7:
            if texto.startswith("8.") or texto.startswith("9.") or (texto and not texto.startswith("7.") and i > 0 and "6." in doc.paragraphs[i-1].text):
                # Verificar si es el final
                break
            para_eliminar.append(i)
    
    # Eliminar en orden inverso para no afectar índices
    for i in reversed(para_eliminar):
        p = doc.paragraphs[i]._element
        p.getparent().remove(p)
        p._p = p._element = None
    
    print(f"✅ Eliminados {len(para_eliminar)} párrafos de la sección 7")

def actualizar_documento():
    """Actualiza el documento Word"""
    doc = Document('PRESENTACION_PROYECTO.docx')
    
    print("📝 Actualizando documento Word...")
    
    # Buscar la sección 3.2 para agregar imágenes
    # Vamos a insertar las imágenes después de la descripción de cada componente
    
    # Primero, encontrar dónde está la sección 3.2
    seccion_3_2_encontrada = False
    indice_3_2 = -1
    
    for i, para in enumerate(doc.paragraphs):
        if "3.2 Componentes Principales" in para.text:
            seccion_3_2_encontrada = True
            indice_3_2 = i
            break
    
    if seccion_3_2_encontrada:
        print("✅ Sección 3.2 encontrada")
        # Insertar imágenes después de la introducción de 3.2
        # Buscar el final de 3.2.1 para insertar primera imagen
        
        # Agregar imágenes después de 3.2.5 (Log de Eventos)
        # Buscar "3.2.5 Log de Eventos"
        for i, para in enumerate(doc.paragraphs):
            if "3.2.5 Log de Eventos" in para.text or "6.2.5 Log de Eventos" in para.text:
                # Insertar imágenes después de esta sección
                indice_insertar = i + 1
                # Buscar el final de esta subsección
                while indice_insertar < len(doc.paragraphs):
                    texto = doc.paragraphs[indice_insertar].text.strip()
                    if texto.startswith("3.3") or texto.startswith("3.4") or texto.startswith("6.3"):
                        break
                    indice_insertar += 1
                
                # Insertar imágenes aquí
                doc.paragraphs[indice_insertar].insert_paragraph_before("")
                p = doc.paragraphs[indice_insertar]
                p.insert_paragraph_before("A continuación se muestran capturas de pantalla de la interfaz:")
                break
    
    # Mejor enfoque: agregar una nueva subsección 3.3 con las imágenes
    # Buscar el final de la sección 3
    for i, para in enumerate(doc.paragraphs):
        if "3.4 Sistema de Estilos" in para.text or "3.5 Flujo" in para.text:
            # Insertar antes de esta sección
            doc.paragraphs[i].insert_paragraph_before("")
            doc.paragraphs[i].insert_paragraph_before("3.3 Capturas de Pantalla de la Interfaz")
            break
    
    # Agregar imágenes
    agregar_imagenes_seccion_interfaz(doc)
    
    # Eliminar sección 7
    eliminar_seccion_7(doc)
    
    # Guardar
    doc.save('PRESENTACION_PROYECTO.docx')
    print("✅ Documento actualizado")
    print(f"   - Párrafos: {len(doc.paragraphs)}")
    print(f"   - Imágenes agregadas en sección de interfaz")
    print(f"   - Sección 7 eliminada")

def agregar_imagenes_seccion_interfaz(doc):
    """Agrega las imágenes en la sección de interfaz"""
    imagenes_path = "Imagenes/"
    imagenes = sorted(glob.glob(os.path.join(imagenes_path, "*.png")))
    
    if not imagenes:
        print("⚠️ No se encontraron imágenes")
        return
    
    # Buscar dónde insertar (después de 3.2.5 o antes de 3.4)
    indice_insertar = -1
    for i, para in enumerate(doc.paragraphs):
        texto = para.text.strip()
        if "3.2.5" in texto or "6.2.5" in texto:
            # Buscar el final de esta subsección
            j = i + 1
            while j < len(doc.paragraphs):
                if doc.paragraphs[j].text.strip().startswith("3.3") or \
                   doc.paragraphs[j].text.strip().startswith("3.4") or \
                   doc.paragraphs[j].text.strip().startswith("6.3"):
                    indice_insertar = j
                    break
                j += 1
            break
    
    if indice_insertar == -1:
        # Buscar "3.4" o "6.3"
        for i, para in enumerate(doc.paragraphs):
            if "3.4 Sistema" in para.text or "6.3 Operaciones" in para.text:
                indice_insertar = i
                break
    
    if indice_insertar > 0:
        # Insertar título de subsección
        doc.paragraphs[indice_insertar].insert_paragraph_before("")
        heading = doc.paragraphs[indice_insertar]
        heading.insert_paragraph_before("3.3 Capturas de Pantalla de la Interfaz")
        doc.paragraphs[indice_insertar].style = 'Heading 3'
        doc.paragraphs[indice_insertar].insert_paragraph_before("")
        
        # Agregar descripción
        doc.paragraphs[indice_insertar].insert_paragraph_before(
            "A continuación se presentan capturas de pantalla de los diferentes componentes de la interfaz del simulador:")
        
        # Agregar imágenes
        descripciones = [
            "Vista completa de la interfaz mostrando todos los paneles",
            "Panel de configuración con todos los controles",
            "Tabla de procesos con diferentes estados",
            "Visualización gráfica del mapa de memoria",
            "Gráfico de Gantt con historial de ejecución",
            "Log de eventos y proceso en ejecución"
        ]
        
        for idx, (img_path, desc) in enumerate(zip(imagenes, descripciones), 1):
            doc.paragraphs[indice_insertar].insert_paragraph_before("")
            p = doc.paragraphs[indice_insertar]
            p.insert_paragraph_before(f"Figura {idx}: {desc}")
            doc.paragraphs[indice_insertar].style = 'Normal'
            doc.paragraphs[indice_insertar].runs[0].bold = True
            
            # Insertar imagen
            p_img = doc.paragraphs[indice_insertar]
            p_img.insert_paragraph_before("")
            p_img = doc.paragraphs[indice_insertar]
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            try:
                run = p_img.add_run()
                run.add_picture(img_path, width=Inches(6.5))
            except Exception as e:
                print(f"⚠️ Error al agregar imagen {img_path}: {e}")
                p_img.add_run(f"[Imagen: {os.path.basename(img_path)}]")
            
            doc.paragraphs[indice_insertar].insert_paragraph_before("")

if __name__ == '__main__':
    actualizar_documento()
