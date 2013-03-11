from googlevoice import Voice
import time

def quantifyTime(msg):
    """returns how old the text message is
    msg is the message
    returns age
    where age is an integer value representing
    the age of the text message in seconds
    (since Jan 01, 2000)"""
    mo = [31, 28, 31, 30, 31, 30,
          31, 31, 30, 31, 30, 31]
    age = 0 #age of text
    t = msg.get("time")
    age += (t.years - 2000) * 365 * 24 * 60 * 60
    for i in range(t.months):
        age += mo[i] * 24 * 60 * 60
    age += t.day * 24 * 60 * 60
    age += t.hour * 60 * 60
    age += t.minute * 60
    age += t.second
    return age
                
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
    msglist.sort(compare)

def compare(msg1, msg2):
    """compares two text messages by date sent
    msg1 is the first message
    msg2 is the second message
    returns 1 if msg1 is older than msg2
    returns -1 if msg1 is newer than msg2
    returns 0 if msg1 and msg2 have same age"""
    age1 = quantifyTime(msg1)
    age2 = quantifyTime(msg2)
    if(age1 > age2): #msg1 is older
        return 1
    if(age1 < age2): #msg1 is newer
        return -1
    return 0 #same age
    
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
