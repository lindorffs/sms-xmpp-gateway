import xmpp
import creds
import gateway as gate

def msgHandler(con, msg):
    print("!!!! GOT XMPP Message From {}: {}".format(msg.getFrom(), msg.getBody()))

class XMPPClient(object):
    def __init__(self):
        try:
         self.client = xmpp.Client(creds.domain, debug=False)
         self.client.connect(server=(creds.server,5222))
         self.client.auth(creds.user, creds.password, "sms to xmpp")
         self.client.sendInitPresence()
         self.client.RegisterHandler('message', msgHandler)
        except:
         pass

    def sendMessage(self, data):
        message = xmpp.Message("1618@"+creds.domain, data)
        message.setAttr("type", "chat")
        try:
         self.client.send(message)
        except:
         pass

    def checkMessages(self):
        self.client.Process()
