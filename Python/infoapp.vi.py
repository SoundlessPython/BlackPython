import time
version = '3.1.0'
date = '10/09/18'
dev = "21mar.16y"

print "This is version %s of infoapp" % version
time.sleep(1)
print "The purpose of this program is to gain more knowladge in python."
time.sleep(2)
print "This program was made on the %s by %s . " % (date, dev)
time.sleep(1)

def accu():
    print """
    This function lists all of the major python concepts that I know .
    1) Strings
    2) Veriables
    3) If Clauses
    4) While Loops
    5) Value
    6) user_input, raw_input and int(input(""))
    7) import time and time.sleep()
    8) Lists
     """
def greating_message():
    print "Good morning %s " % Username
def accs():
    print """
    name: sam"""
def accj():
    print """
    name: Jack
    """
username = raw_input("Username : ")
time.sleep(1)
password = raw_input("Password : ")
time.sleep(1)
print "Let me check those details......"
time.sleep(2)
key = int(input("As a last security messure, please enter the date I was created : "))

if username == 'umar':
    if password == '2121':
        accu()
    while password != '2121':
        password = raw_input("Password : ")
        if password == 'uuuu':
            accu()
elif username == 'sam':
    if password == 'ssss':

        accs()
    while password != 'ssss':
        password = raw_input("password : ")
        if password == 'ssss':
            accs()
elif username == 'jack':
    if password == '1010':
        accj()
    while password != '1010':
        password = raw_input("password : ")
        if password == '1010':
            accj()
opp = raw_input("Do you require any other services? ")
while opp == 'yes':
    username = raw_input("Username : ")
    time.sleep(1)
    password = raw_input("Password : ")

    if username == 'umar':
        if password == '2121':
            accu()
        while password != '2121':
            password = raw_input("Password : ")
            if password == 'uuuu':
                accu()
    elif username == 'sam':
        if password == 'ssss':

            accs()
        while password != 'ssss':
            password = raw_input("password : ")
            if password == 'ssss':
                accs()
    elif username == 'jack':
        if password == 'jjjj':
            accj()
        while password != 'jjjj':
            password = raw_input("password : ")
            if password == 'jjjj':
                accj()
    opp = raw_input("Do you require any other services? ")
if opp != 'yes':
    time.sleep(1)
    print "Thanks for using infoapp."
