#!/usr/bin/env python3
"""HTTPS dev server for あしあと AR app."""
import ssl, http.server, os

PORT = 8443
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('/tmp/cert.pem', '/tmp/key.pem')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} {args[0]}")

httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print(f"\n  ✅ HTTPS サーバー起動中")
print(f"\n  PC ブラウザ  : https://localhost:{PORT}")
print(f"  スマホ       : https://192.168.210.66:{PORT}")
print(f"\n  ⚠️  スマホで「この接続はプライバシーが保護されていません」")
print(f"      と表示されたら「詳細設定」→「続行」を選んでください")
print(f"\n  Ctrl+C で停止\n")
httpd.serve_forever()
