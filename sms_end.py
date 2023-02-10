from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote_plus
import threading

messages_in = []

class smsListener(BaseHTTPRequestHandler):
    def do_GET(self):
        def msgFormat(msg):
            return("!!!! GOT SMS Message From {}: {}".format(msg["From"], msg["Body"]))
        data = urlparse(self.path).query
        data = dict(entry.split("=") for entry in data.split("&"))
        for key in data.keys():
            data[key] = unquote_plus(data[key])
        messages_in.append(data)
        try:
         print(msgFormat(data))
        except:
         pass

class smsServer:
    def __init__(self):
        try:
         self.httpd = HTTPServer(("0.0.0.0", 14444), smsListener)
        except:
         pass

class protector:
    server = smsServer()
    thread = threading.Thread(target=server.httpd.serve_forever)
    def __init__(self):
        pass
    def checkMessages(self):
        global messages_in
        ret = messages_in
        messages_in = []
        return(ret)

smsHandler = protector()
