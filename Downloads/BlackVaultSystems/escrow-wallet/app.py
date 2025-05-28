from http.server import BaseHTTPRequestHandler, HTTPServer

class EscrowWalletHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"module": "escrow-wallet", "status": "ready"}')

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), EscrowWalletHandler)
    print("Serving escrow-wallet on port 8000...")
    server.serve_forever()