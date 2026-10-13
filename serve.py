# Servidor local sin caché: siempre muestra la última versión de la página.
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class NoCache(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    print('Abre http://localhost:5173')
    ThreadingHTTPServer(('', 5173), NoCache).serve_forever()
