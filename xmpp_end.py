import xmpp
import creds
import gateway as gate

def msgHandler(con, msg):
    print("!!!! GOT XMPP Message From {}: {}".format(msg.getFrom(), msg.getBody()))

class XMPPClient(object):
    def __init__(self):
        self.client = xmpp.Client(creds.domain, debug=False)
        self.client.connect(server=(creds.server,5222))
        self.client.auth(creds.user, creds.password, "sms to xmpp")
        self.client.sendInitPresence()
        self.client.RegisterHandler('message', msgHandler)

    def sendMessage(self, data):
        message = xmpp.Message("1618@"+creds.domain, data)
        message.setAttr("type", "chat")
        self.client.send(message)

    def checkMessages(self):
        self.client.Process()
