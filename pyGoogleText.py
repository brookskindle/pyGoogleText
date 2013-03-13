from googlevoice import Voice
import time

def quantifyTime(msg):
    """returns how old the text message is
    msg is the message
    returns age
    where age is an integer value representing
    the age of the text message in seconds
    (since Jan 01, 2000)"""
    age = 0 #age of text
    t = msg.get("startTime")

    age += (t.tm_year - 2000 - 1) * 365 * 24 * 60 * 60 #years
    age += (t.tm_yday - 1) * 24 * 60 * 60 #days
    age += (t.tm_hour - 1) * 60 * 60 #hours
    age += (t.tm_min - 1) * 60 #minutes
    age += t.tm_sec - 1 #seconds
    age += t.tm_isdst * 60 * 60 #daylight savings time
    
    return age
                
def getLogin():
    """prompts user for gvoice login info
    returns usr, pw
    where usr is the email
    and pw is the password"""
    usr = raw_input("Enter google email address: ")
    pw = raw_input("Enter password: ")
    return usr, pw

def getPhone():
    """prompts user for a phone number to monitor
    returns phone
    where phone is the phone number"""
    pr = "Which phone number do you want to monitor "
    pr += "texts from? "
    phone = raw_input(pr)
    return phone

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
    where msglist is the unread message
    list sorted from newest to oldest"""
    sms = gvoice.sms()
    unread = []
    for msg in sms.messages:
        if(not isRead(msg)): #unread sms
            unread.append(msg)
    sortMostRecent(unread)
    return unread #return sorted, unread list of sms

def isRead(msg):
    """returns if a text message has already been read"""
    return msg.get("isRead")

def markMessage(msg, isRead = 1):
    """marks the message as either read
    or unread (default mark as read)
    msg is the message to be marked
    isRead is the status to mark the message
    as, 1 for read, 0 for unread
    does not return anything"""
    msg.mark(isRead)

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
    gvoice.send_sms(phone, msg)

def wait(secs = 60):
    """waits a given number of seconds"""
    time.sleep(secs)

def test():
    """tester function, tests the program"""
    usr, pw = getLogin()
    #query = getPhone()
    print "Loggin' in..."
    v = Voice()
    v.login(usr, pw)
    print "Displayin' unread texts..."
    unread = getUnreadTexts(v)
    for msg in unread:
        print msg.get("messageText")

def main():
    test() #test the program

if __name__ == "__main__":
    main()
