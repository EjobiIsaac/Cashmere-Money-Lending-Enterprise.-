import webbrowser, os, threading, http.server, socketserver
PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
webbrowser.open(f"http://localhost:{PORT}/index.html")
print("CASHMERE RUNNING... Do not close this window")
input("Press ENTER to close...")
