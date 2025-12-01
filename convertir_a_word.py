#!/usr/bin/env python3
"""
Script para convertir PRESENTACION_PROYECTO.md a formato Word
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re

def procesar_texto_con_formato(parrafo, texto):
    """Procesa texto Markdown y aplica formato (negrita, código)"""
    # Dividir por **texto**
    partes = re.split(r'(\*\*[^*]+\*\*)', texto)
    
    for parte in partes:
        if parte.startswith('**') and parte.endswith('**'):
            # Texto en negrita
            run = parrafo.add_run(parte[2:-2])
            run.bold = True
        elif parte.startswith('`') and parte.endswith('`'):
            # Código inline
            run = parrafo.add_run(parte[1:-1])
            run.font.name = 'Consolas'
        else:
            # Texto normal
            if parte.strip():
                parrafo.add_run(parte)

def crear_documento_word():
    """Crea un documento Word a partir del contenido del Markdown"""
    
    # Leer el archivo Markdown
    with open('PRESENTACION_PROYECTO.md', 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Crear documento Word
    doc = Document()
    
    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
    
    # Procesar el contenido línea por línea
    lineas = contenido.split('\n')
    i = 0
    en_codigo = False
    codigo_actual = []
    
    while i < len(lineas):
        linea = lineas[i]
        linea_stripped = linea.strip()
        
        # Manejar bloques de código
        if linea_stripped.startswith('```'):
            if en_codigo:
                # Cerrar bloque de código
                if codigo_actual:
                    p = doc.add_paragraph()
                    run = p.add_run('\n'.join(codigo_actual))
                    run.font.name = 'Consolas'
                    run.font.size = Pt(9)
                    p.style = 'Intense Quote'
                codigo_actual = []
                en_codigo = False
            else:
                en_codigo = True
            i += 1
            continue
        
        if en_codigo:
            codigo_actual.append(linea)
            i += 1
            continue
        
        # Saltar líneas vacías (pero no demasiadas seguidas)
        if not linea_stripped:
            # Solo agregar un espacio si el último párrafo no estaba vacío
            if i + 1 < len(lineas) and lineas[i+1].strip():
                i += 1
                continue
            else:
                i += 1
                continue
        
        # Título principal (#)
        if linea_stripped.startswith('# '):
            texto = linea_stripped[2:].strip()
            p = doc.add_heading(texto, level=0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            i += 1
        
        # Subtítulo nivel 1 (##)
        elif linea_stripped.startswith('## '):
            texto = linea_stripped[3:].strip()
            doc.add_heading(texto, level=1)
            i += 1
        
        # Subtítulo nivel 2 (###)
        elif linea_stripped.startswith('### '):
            texto = linea_stripped[4:].strip()
            doc.add_heading(texto, level=2)
            i += 1
        
        # Subtítulo nivel 3 (####)
        elif linea_stripped.startswith('#### '):
            texto = linea_stripped[5:].strip()
            doc.add_heading(texto, level=3)
            i += 1
        
        # Separador (---)
        elif linea_stripped.startswith('---'):
            doc.add_paragraph()
            i += 1
        
        # Lista con viñetas (-)
        elif linea_stripped.startswith('- '):
            texto = linea_stripped[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            procesar_texto_con_formato(p, texto)
            i += 1
            
            # Continuar con sub-elementos de la lista (indentados)
            while i < len(lineas):
                siguiente = lineas[i].strip()
                if siguiente.startswith('- ') and len(lineas[i]) - len(lineas[i].lstrip()) > 2:
                    # Sub-elemento
                    sub_texto = siguiente[2:].strip()
                    p = doc.add_paragraph(style='List Bullet 2')
                    procesar_texto_con_formato(p, sub_texto)
                    i += 1
                elif siguiente.startswith('- '):
                    # Nuevo elemento de lista principal
                    break
                elif siguiente.startswith('#') or siguiente.startswith('---') or not siguiente:
                    # Fin de la lista
                    break
                else:
                    # Continuación del texto anterior
                    p = doc.paragraphs[-1]
                    p.add_run(' ')
                    procesar_texto_con_formato(p, siguiente)
                    i += 1
        
        # Lista numerada
        elif re.match(r'^\d+\.\s', linea_stripped):
            texto = re.sub(r'^\d+\.\s', '', linea_stripped)
            p = doc.add_paragraph(style='List Number')
            procesar_texto_con_formato(p, texto)
            i += 1
        
        # Texto normal
        else:
            p = doc.add_paragraph()
            procesar_texto_con_formato(p, linea_stripped)
            i += 1
    
    # Guardar el documento
    doc.save('PRESENTACION_PROYECTO.docx')
    print("✅ Documento Word creado exitosamente: PRESENTACION_PROYECTO.docx")
    print(f"   Total de párrafos: {len(doc.paragraphs)}")

if __name__ == '__main__':
    crear_documento_word()
