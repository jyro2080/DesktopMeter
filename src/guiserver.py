#!/usr/bin/env python

import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import threading

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


class GUIServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.httpd = BaseHTTPServer.HTTPServer(('',PORT), GUIRequestHandler)
        self.keep_running = True

    def run(self):
        while self.keep_running:
            self.httpd.handle_request()
