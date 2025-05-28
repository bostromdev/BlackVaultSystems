from http.server import BaseHTTPRequestHandler, HTTPServer

class SecureMessagingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"module": "secure-messaging", "status": "ready"}')

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SecureMessagingHandler)
    print("Serving secure-messaging on port 8000...")
    server.serve_forever()