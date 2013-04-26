#there may be errors if you try to include quotes in
#your message. got a ParsingError as I was texting
#with weird symbols in my message. Message sent ok,
#but was 2 fetches later a parseError occured
#(4/24/13)
#reformated names and spacing to be consistent with python naming conventions
#http://www.python.org/dev/peps/pep-0008/#function-names

from googlevoice import Voice
import time
import shelve
import os
from ParseError import ParseError

creds = {}  # where we can store login credentials


def quantify_time(msg):
    """returns how old the text message is
    msg is the message
    returns age
    where age is an integer value representing
    the age of the text message in seconds
    (since Jan 01, 2000)"""
    age = 0  # age of text
    t = msg.get("startTime")

    age += (t.tm_year - 2000 - 1) * 365 * 24 * 60 * 60  # years
    age += (t.tm_yday - 1) * 24 * 60 * 60  # days
    age += (t.tm_hour - 1) * 60 * 60  # hours
    age += (t.tm_min - 1) * 60  # minutes
    age += t.tm_sec - 1  # seconds
    age += t.tm_isdst * 60 * 60  # daylight savings time

    return age


def get_login():
    """prompts user for gvoice login info
    returns usr, pw
    where usr is the email
    and pw is the password"""
    if not creds:
        usr = raw_input("Enter google email address: ")
        pw = raw_input("Enter password: ")
        creds["usr"] = usr
        creds["pw"] = pw
    else:
        usr = creds["usr"]
        pw = creds["pw"]
    return usr, pw


def get_phone():
    """prompts user for a phone number to monitor
    returns phone
    where phone is the phone number"""
    pr = "Which phone number do you want to monitor "
    pr += "texts from? "
    phone = raw_input(pr)
    return phone


def sort_most_recent(msglist):
    """sorts message list from newest to oldest"""
    msglist.sort(compare_by_date)


def compare_by_date(msg1, msg2):
    """compares two text messages by date sent
    msg1 is the first message
    msg2 is the second message
    returns 1 if msg1 is older than msg2
    returns -1 if msg1 is newer than msg2
    returns 0 if msg1 and msg2 have same age"""
    age1 = quantify_time(msg1)
    age2 = quantify_time(msg2)
    if age1 > age2:  # msg1 is older
        return 1
    if age1 < age2:  # msg1 is newer
        return -1
    return 0  # same age


def get_unread_texts(gvoice, ph):
    """returns a sorted message list of unread texts from a given phone number
    gvoice is the Voice() instance
    ph is the phone number
    returns msglist
    where msglist is the unread message
    list sorted from newest to oldest"""
    sms = gvoice.sms()
    unread = []
    for msg in sms.messages:
        if not is_read(msg) and msg.get("phoneNumber").find(ph) != -1:  # unread sms from the monitored phone number
            unread.append(msg)
    sort_most_recent(unread)
    return unread  # return sorted, unread list of sms


def is_read(msg):
    """returns if a text message has already been read"""
    return msg.get("isRead")


def mark_message(msg, isRead=1):
    """marks the message as either read
    or unread (default mark as read)
    msg is the message to be marked
    isRead is the status to mark the message
    as, 1 for read, 0 for unread
    does not return anything"""
    msg.mark(isRead)


def get_msg_children(msg):
    """get child message does not work! It has to do with the
    parser and how google presents data. Too complicated to work with
    """
    print msg.children()
    return msg.children()  # does this work?


def delete_message(msg, move2Trash=1):
    """deletes the message. Use after sending
    the message off to the intended recipient. 
    This is so that when the othe person replies
    he does not get a repeat message, since only
    the first message generally shows up as unread,
    and would continually send off that same first msg"""
    msg.delete(move2Trash)  # if we call msg.delete(0) that un-deletes the msg


def cleanup_phone_number(number):
    """this removed non-numeric characters from
    a string to return a cleaned up phone number"""
    badBits = ['(', ')', ' ', '-']
    for badBit in badBits:
        number.replace(badBit, '')
    return number


def parse_msg(msg):
    """returns a phone number and message
        hidden inside of a message (ie, parsing
        the message so long as the message is
        in the format "<phone-number> <message>"
        msg is the text message
        returns phone, message
        where phone is the phone number
        and message is the text message"""
    parts = msg.split()
    number = parts[0]
    #remove extraneous characters from number
    number = cleanup_phone_number(number)
    try:
        num = int(number)  # try to convert phone number to integer
    except:
        raise ParseError  # unable to parse phone number correctly
    msg = ""
    for part in parts[1:-1]:  # parts[0] is the #. This excludes the last part, which will be added after the for-loop
        msg += part + ' '
    msg += parts[-1]  # prevent appending ' ' to end of message
    return number, msg


def text_fwd(gvoice, phone, msg):
    """texts a phone number with the given message
    gvoice is the Voice() instance
    phone is the desired phone number
    msg is the message"""
    gvoice.send_sms(phone, msg)


def wait(secs=60):
    """waits a given number of seconds"""
    time.sleep(secs)


def print_msgs(msgs):
    for msg in msgs:
        print msg.get("messageText")


def get_voice_object():  # I would like to somehow remove all these shelving protocols and embed in a constructed class
    if creds.has_key("v"):
        v = creds["v"]  # get the stored voice object, so we don't keep creating a new one
    else:
        v = Voice()
        creds["v"] = v
    return v


def run_cmd_program():
    """runs the command line version of the program"""
    load_creds()
    usr, pw = get_login()  # login credentials
    query = get_phone()  # get phone number to monitor
    query = cleanup_phone_number(query)  # removes non-numeric characters from number
    print "Loggin' in..."
    v = get_voice_object()
    v.login(usr, pw)
    print "Displayin' unread texts..."
    while True:  # infinite loop to keep monitoring for unread texts
        unread = get_unread_texts(v, query)
        for new in unread:  # loop unread messages
            try:
                msg = new.get("messageText")  # text message in string form (msg)
                ph, txt = parse_msg(msg)  # split string into phone number and text message parts
            except ParseError:  # invalid message
                print "Unable to parse message", new, "...skipping"
            else:
                mark_message(new)  #if we delete message, then maybe child msg can get read next, not marked read
                v.send_sms(ph, txt)  # forward text to the specified recipient
                v.send_sms(query, "sent txt to " + ph)  # tell the user that his msg got through.
                print "Text sent to " + ph + " : \"" + txt + "\""
            delete_message(new)  # delete message regardless if processed or not. if you mess up a fwd text, deleting it
                                 # is the ONLY way to make sure that your next message is properly processed / in front
        secs = 5*60
        print "Waiting", secs, "second(s) before fetching unread texts"
        wait(secs)


def store_creds():
    credstore = shelve.open("creds")
    for key in creds:
        if not key == "v":
            credstore[key] = creds[key]
    credstore.sync()


def load_creds():
    try:
        credstore = shelve.open("creds")
    except:
        print "oops couldn't load creds from file"
        return
    creds.clear()  # clear creds so that we can load different credentials if necessary
    for key in credstore:
        creds[key] = credstore[key]


def erase_creds():
    creds.clear()
    store_creds()


def refresh_creds():
    creds.pop('v')
    creds["v"] = get_voice_object()  # gets a new gv object, which can be used to login as if new. Same usr and pw tho


def main():
    run_cmd_program()  # test the program


if __name__ == "__main__":
    main()
