#textme pls

from googlevoice import Voice
import time
v = Voice()

#hard code login
usr = "brookskindle@gmail.com"
pw = "snake5"
v.login(usr, pw)

#returns the most recent unread text
#message by the given phone number
def parseInbox(phone = "5093506691"):
    #get list of text messages sent by the given phone number
    inbox = v.search(phone)
    return inbox

#returns the id of the most recent
#unread message of the given texts
def mostRecentUnread(messages):
    unread = []
    sort = []
    for msg in messages: #loop messages
        if not msg.get("isRead"): #unread message
            unread.append(msg)
    #sort messages by most recent first
    while unread:
        earliest = 0
        for i in range(len(unread) - 1): #loop unread messages
            f = quantifyTime(unread[i].get("startTime"))
            s = quantifyTime(unread[i + 1].get("startTime"))
            if (f > quantifyTime(unread[0].get("startTime"))):
                earliest = unread[i]

#accepts a struct time (from a message)
#and quantifies it, returning an integer
#value representing the number of seconds
#since Jan 01, 2000
def quantifyTime(time):
    pass
                
def getLogin():
    pass

def getPhone():
    pass

def sortMostRecent(msglist):
    pass

def getUnread(gvoice):
    pass

def markMessage(msg):
    pass

def splitMessage(msg):
    parts = msg.split()
    number = int(parts[0])
    msg = ""
    for part in parts[1:]:
        msg += part
    return number, msg

def textfwd(gvoice, phone, msg):
    pass

def wait(minutes = 5):
    time.sleep(minutes * 60)
    pass


#loop infinitely
while(True):
    time.sleep(5) #sleep 5 seconds before re-checking texts
    msg = parseInbox() #assume this is the text message you want to analyze
    parts = msg.split()
    fwdnumber = int(parts[0])
    fwdmsg = ""
    #get message to send
    for i in range(1,len(parts)):
        fwdmsg += parts[i]

    v.send_sms(fwdnumber, fwdmsg)
