#!/usr/bin/env python3
"""
Script para verificar y preparar el archivo Word para descarga
"""

import os
import shutil
from pathlib import Path

def main():
    archivo_word = "PRESENTACION_PROYECTO.docx"
    
    if os.path.exists(archivo_word):
        # Obtener información del archivo
        tamaño = os.path.getsize(archivo_word)
        tamaño_kb = tamaño / 1024
        
        print("=" * 60)
        print("📄 ARCHIVO WORD ENCONTRADO")
        print("=" * 60)
        print(f"Nombre: {archivo_word}")
        print(f"Ubicación: {os.path.abspath(archivo_word)}")
        print(f"Tamaño: {tamaño_kb:.2f} KB ({tamaño:,} bytes)")
        print("=" * 60)
        print("\n✅ El archivo está listo para descargar.")
        print("\n📋 INSTRUCCIONES PARA DESCARGAR:")
        print("1. Busca 'PRESENTACION_PROYECTO.docx' en el explorador de archivos")
        print("2. Haz clic derecho sobre el archivo")
        print("3. Selecciona 'Download' o 'Save As'")
        print("\n💡 Si no lo ves, intenta:")
        print("   - Actualizar el explorador (F5)")
        print("   - Buscar 'PRESENTACION_PROYECTO.docx' en la búsqueda de archivos")
        print("   - Verificar que no esté oculto por filtros")
        print("=" * 60)
        
        # Verificar permisos
        if os.access(archivo_word, os.R_OK):
            print("✅ Permisos de lectura: OK")
        else:
            print("❌ Error: Sin permisos de lectura")
            
    else:
        print("❌ Error: El archivo no se encontró")
        print("   Intentando recrearlo...")
        # Aquí podrías llamar a convertir_a_word.py si es necesario

if __name__ == '__main__':
    main()
