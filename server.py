import http.server
import socketserver
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/myfile.html':
            self.send_response(302)  # Redirect code
            self.send_header('Location', 'http://example.com/myfile.html')
            self.end_headers()
        else:
            super().do_GET()

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
