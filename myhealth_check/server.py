from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')


httpd = HTTPServer(('', 9091), SimpleHTTPRequestHandler)
httpd.serve_forever()
