from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        print("Received code:", params.get('code'))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"You can close this window now.")

httpd = HTTPServer(('localhost', 8080), Handler)
print("Listening on http://localhost:8080")
httpd.serve_forever()