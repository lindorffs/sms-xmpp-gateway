# sms-xmpp-gateway
Handles SMS to XMPP and XMPP to SMS communications

##
WARNING: USE AT YOUR OWN RISK.

##
Take in SMS from Twilio as an HTTP GET and pipe it to XMPP, and vice versa.

## Usage:

Create a creds.py file with:
server = "your.xmpp.server"
domain = "your.xmpp.domain"
user = "yourXmppUser"
password = "yourXmppPassword"

Point your Twilio SMS endpoint to your server at port 14444 using GET requests.

Run gateway.py.
