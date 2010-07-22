#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

PORT = 6006

tmp = '''
<html>
<head>
<title>AJAX</title>
</head>
<body>HI THERE</body>
</html>
'''

class GUIRequestHandler(SimpleHTTPRequestHandler):

    def do_HEAD(self):
        SimpleHTTPRequestHandler.do_HEAD(self)

    def do_GET(self):
        if self.path.startswith('/ajax/'):
            self.send_response(200);
            self.send_header("Content-Type", "text/html")
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(tmp)
        else:
            SimpleHTTPRequestHandler.do_GET(self)



def run_gui():
    httpd = SocketServer.TCPServer(("", PORT), GUIRequestHandler)
    print "serving at port", PORT
    httpd.serve_forever()
