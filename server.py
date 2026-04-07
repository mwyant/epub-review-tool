import http.server
import ssl
import os
import socket

PORT = 8002
DIRECTORY = "/app" if os.path.exists("/app") else os.getcwd()
os.chdir(DIRECTORY)

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('X-Content-Type-Options', 'nosniff')
        # Robust CSP
        csp = ("default-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net https://unpkg.com blob:; "
               "worker-src 'self' blob:; "
               "img-src 'self' data: blob:;")
        self.send_header('Content-Security-Policy', csp)
        super().end_headers()

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6 if socket.has_ipv6 else socket.AF_INET

def run():
    # Try IPv6/IPv4 dual stack if available, else standard IPv4
    try:
        httpd = HTTPServerV6(('::', PORT), Handler)
    except:
        httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)

    if os.path.exists("cert.pem") and os.path.exists("key.pem"):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print(f"Serving securely at https://localhost:{PORT}")
    else:
        print(f"Serving at http://localhost:{PORT} (No SSL)")

    httpd.serve_forever()

if __name__ == "__main__":
    run()
