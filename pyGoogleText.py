from googlevoice import Voice
import time

def quantifyTime(msg):
    """returns how old the text message is
    msg is the message
    returns an integer value representing
    the age of the text message (starting
    from Jan 01, 2000)"""
    pass
                
def getLogin():
    """prompts user for gvoice login info
    returns usr, pw
    where usr is the email
    and pw is the password"""
    pass

def getPhone():
    """prompts user for a phone number to monitor
    returns phone
    where phone is the phone number"""
    pass

def sortMostRecent(msglist):
    """sorts message list from newest to oldest"""
    pass

def getUnreadTexts(gvoice):
    """returns a sorted message list of unread texts
    gvoice is the Voice() instance
    returns msglist
    where msglist is a message list sorted from
    newest to oldest"""
    pass

def markMessage(msg):
    """marks the message as read
    msg is the message to be marked
    does not return anything"""
    pass

def splitMessage(msg):
    """returns a phone number and message
    hidden inside of a message (ie, parsing
    the message so long as the message is
    in the format "<phone-number> <message>"
    msg is the text message
    returns phone, message
    where phone is the phone number
    and message is the text message"""
    parts = msg.split()
    number = int(parts[0])
    msg = ""
    for part in parts[1:]:
        msg += part
    return number, msg

def textfwd(gvoice, phone, msg):
    """texts a phone number with the given message
    gvoice is the Voice() instance
    phone is the desired phone number
    msg is the message"""
    pass

def wait(minutes = 5):
    """waits a given number of minutes"""
    time.sleep(minutes * 60)
    pass

def main():
    pass

if __name__ == "__main__":
    main()
