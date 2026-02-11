#!/usr/bin/env python3
"""
Simple HTTP Server for Nepal Community SACCOS Website
This server will make the website accessible via IP address on port 8000
"""

import http.server
import socketserver
import os
import socket

# Change to the website directory
os.chdir('/mnt/user-data/outputs/saccos_complete_site')

PORT = 8000

# Get the server's IP address
def get_ip_address():
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except:
        return "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

# Create the server
Handler = MyHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

ip = get_ip_address()

print("=" * 70)
print("🌐 Nepal Community SACCOS Website Server")
print("=" * 70)
print(f"\n✅ Server is running!")
print(f"\n📍 Access the website at:")
print(f"   • Local:    http://localhost:{PORT}")
print(f"   • Network:  http://{ip}:{PORT}")
print(f"\n💡 Share this URL with anyone on the same network:")
print(f"   http://{ip}:{PORT}")
print(f"\n⚠️  To stop the server, press Ctrl+C")
print("=" * 70)
print("\n")

# Start serving
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n🛑 Server stopped.")
    httpd.server_close()
