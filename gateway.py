import sms_end
import xmpp_end
import threading
import time
import globalDefs

version_name = "Leaping Lemur"

class gateway:
    smsHandler = sms_end.smsHandler
    xmppHandler = None
    loopHandler = None
    running = False
    def __init__(self):
        print("!!!! SMS-XMPP GATEWAY V. {} Initializing.".format(version_name))
        self.loopHandler = threading.Thread(target=self.loop)
        self.smsThread = self.smsHandler.thread
        print("!!!! SMS Server starting.")
        self.smsThread.start()
        print("!!!! XMPP Client starting.")
        self.xmppHandler = xmpp_end.XMPPClient()
        print("!!!! Initialization finished.")
        self.start()
    
    def checkMessages(self):
        ret = self.smsHandler.checkMessages()
        self.xmppHandler.checkMessages()
        return ret

    def loop(self):
        def msgFormat(msgData):
            return("FROM: {}\nRCVD: 00.00.00 @ 00:00SM\nBODY:\n{}".format(msgData["From"],msgData["Body"]))
        while globalDefs.running:
            msgs = self.checkMessages()
            if (msgs):
                for msg in msgs:
                    to_send = msgFormat(msg)
                    self.xmppHandler.sendMessage(to_send)
            time.sleep(1)
        print("!!!! Gateway Loop Finished.")

    def start(self):
        print("!!!! SMS-XMPP GATEWAY V. {} Starting.".format(version_name))
        globalDefs.running = True
        self.loopHandler.start()

if __name__ == "__main__":
    gate = gateway()
