from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        hostname = socket.gethostname()
        message = f"Hello from pod: {hostname}\n"


        self.wfile.write(message.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()

    