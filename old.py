#textme pls

from googlevoice import Voice
import time
v = Voice()

#hard code login
usr = ""
pw = ""
v.login(usr, pw)

#returns the most recent unread text
#message by the given phone number
def parseInbox(phone = ""):
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