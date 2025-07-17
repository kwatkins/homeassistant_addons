from http.server import HTTPServer, BaseHTTPRequestHandler


import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

port = int(os.environ.get('PORT', 9091))
httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
httpd.serve_forever()
