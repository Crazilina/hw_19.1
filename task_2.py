from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        filepath = os.path.join(os.getcwd(), 'index.html')

        try:
            with open(filepath, 'rb') as html_file:
                content = html_file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: %s' % self.path)


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 8080
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
