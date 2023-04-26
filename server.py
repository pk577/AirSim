import http.server
import socketserver

PORT = 1337

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    ".js":"application/javascript"
})

httpd = socketserver.TCPServer(("",PORT), Handler)
try:
    print(f"serving at http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
    exit(0)