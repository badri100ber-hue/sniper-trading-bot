import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class BotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/api/status"):
            data = {
                "name": "Sniper Trading Bot",
                "status": "online",
                "mode": "simulation",
                "live_trading_enabled": False,
                "market_data_connected": False,
                "broker_connected": False,
                "message": "Aucune connexion réelle au marché ou au broker."
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_error(404, "Route introuvable")

    def log_message(self, format, *args):
        print(format % args)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), BotHandler)
    print(f"Sniper Trading Bot actif sur le port {port}")
    server.serve_forever()