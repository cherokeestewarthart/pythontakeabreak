import sys
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class CherokeeHandler(BaseHTTPRequestHandler):        
    def do_GET(self):
        print(self.path)
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write("FUCK YOU")

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

CherokeeHandler.protocol_version = "HTTP/1.0"
httpd = HTTPServer(server_address, CherokeeHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
