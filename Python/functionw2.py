import time
updates = "nothing new"
notifications = "I don't know what this does."
username = raw_input("Enter username: ")
# I will add time.sleep(2) when I have finished testing
password = raw_input("Enter password: ")
greating = "HEllo"
def account_umar(updates, notifications):
    # Umar's account
    print """
    Name: Umar Sulaiman
    DOB: 21/02/18
    Email: umar212online@gmail.com
    """
def account_ahmed(updates, notifications):
    print """
    Name: Ahmed Muhammad
    DOB: 01/02/95
    Email: ahmed@gmail.com
    """
def login_message(username, greating):
    print("Hello, %s ,I hope you enjoy your visit.") % username
if username == 'umar':
    if password == 'u':
        login_message(username, greating)
        req = raw_input("So, how can I help you today? ")
        if req == 'info':
            account_umar(updates, notifications)
        elif req == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "You have entered the wrong password."
elif username == 'ahmed':
    if password == 'a':
        login_message(username, greating)
        req2 = raw_input("So, how can I help you today? ")
        if req2 == 'info':
            account_ahmed(updates, notifications)
        elif req2 == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "You have entered the wrong password."
