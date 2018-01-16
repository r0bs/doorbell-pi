import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from doorOpener import openDoor

hostName = "localhost"
hostPort = 80

class CommandHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        token = self.path[1:]
        isTokenValid = self.server.tokenHandler.validateToken(bytes(token, "utf-8"))
        if(isTokenValid):
            openDoor()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Srrrr....</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><h1>Srrrr....</h1>", "utf-8"))
            self.wfile.write(bytes("<p>Opening the door.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Nope</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>Door stays closed.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

class CommandServer:

    def __init__(self, tokenHandler):
        server = HTTPServer((hostName, hostPort), CommandHandler)
        server.tokenHandler = tokenHandler
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

        server.server_close()
        print(time.asctime(), "Door Server Stops - %s:%s" % (hostName, hostPort))

    print(time.asctime(), "Door Server Starts - %s:%s" % (hostName, hostPort))

    