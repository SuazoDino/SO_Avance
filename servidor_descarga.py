#!/usr/bin/env python3
"""
Servidor simple para descargar el archivo Word
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Permitir descarga de archivos
        if self.path.endswith('.docx'):
            self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            self.send_header('Content-Disposition', f'attachment; filename="PRESENTACION_PROYECTO.docx"')
        super().end_headers()

if __name__ == '__main__':
    os.chdir('/workspace')
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🌐 SERVIDOR DE DESCARGA INICIADO")
        print("=" * 60)
        print(f"\n📥 Abre tu navegador y ve a:")
        print(f"   http://localhost:{PORT}/PRESENTACION_PROYECTO.docx")
        print(f"\n   O descarga desde:")
        print(f"   http://localhost:{PORT}/")
        print("\n⏹️  Presiona Ctrl+C para detener el servidor")
        print("=" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Servidor detenido")
