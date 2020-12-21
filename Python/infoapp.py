import time
updates = "nothing new"
notifications = "I don't know what this does."
username = raw_input("Enter username: ")
time.sleep(2)
password = raw_input("Enter password: ")
time.sleep(1)
print "Just one momment please."
time.sleep(2)
greating = "HEllo"
list = ['info', 'help', 'log out']
def account_test1(updates, notifications):
    # Umar's account
    print """
    Name: Test 1
    DOB: 21/02/02
    Email: test1@gmail.com
    Age: 16
    Hobbies: coding, reading, skateboarding
    Food: bannanas
    """
def account_test2(updates, notifications):
    print """
    Name: Test 2
    DOB: 01/02/95
    Email: test2@gmail.com
    Age: 25
    Hobbies: shopping
    Food: crisps
    """
def account_test3(updates, notifications):
    print """
    Name: Test 3
    DOB: 16/04/05
    Email: test3@gmail.com
    Age: 13
    Hobbies: smartphone
    Food: sweets
    """
def account_test4(updates, notifications):
    print """
    Name: Test 4
    DOB: 22/12/07
    Email: test4@gmail.com
    Age: 14
    Hobbies: Shouting
    Food: marshmellows
    """
def account_test5(updates, notifications):
    print """
    Name: Test 5 
    DOB: 18/04/85
    Email: test5@gmail.com
    Age: 33
    Hobbies: singing
    Food: Tuna
    """
    # account_xxxxx is a function containing account information
def login_message(username, greating):
    print("Hello, %s ,I hope you enjoy your visit.") % username
if username == 'ac100':
    if password == '10100':
        login_message(username, greating)
        req = raw_input("So, how can I help you today? ")
        if req == 'info':
            account_test1(updates, notifications)
        elif req == 'options':
            for item in list:
                print item
            req = raw_input("So, how can I help you today? ")
            if req == 'info':
                account_test1(updates, notifications)
            elif req == 'log out':
                time.sleep(2)
                print "You have been succesfully loged out."
        elif req == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password."

# End of account_test1
elif username == 'ac200':
    if password == '14112131':
        login_message(username, greating)
        req2 = raw_input("So, how can I help you today? ")
        if req2 == 'info':
            account_test2(updates, notifications)
        elif req2 == 'options':
            for item in list:
                print item
            req2 = raw_input("So, how can I help you today? ")
            if req2 == 'info':
                account_test2(updates, notifications)
            elif req2 == 'log out':
                time.sleep(2)
                print "You have been succesfully loged out."
        elif req2 == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password."

# End of account_test2
elif username == 'ac300':
    if password == '14112131':
        login_message(username, greating)
        req3 = raw_input("So, how can I help you today? ")
        if req3 == 'info':
            account_test3(updates, notifications)
        elif req3 == 'options':
            for item in list:
                print item
            req3 = raw_input("So, how can I help you today? ")
            if req3 == 'info':
                account_test3(updates, notifications)
            elif req3 == 'log out':
                time.sleep(2)
                print "You have been succesfully loged out."
        elif req3 == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password."
# End of account_test3
elif username == 'test4':
    if password == '14112131':
        login_message(username, greating)
        req4 = raw_input("So, how can I help you today? ")
        if req4 == 'info':
            account_hafsa(updates, notifications)
        elif req4 == 'options':
            for item in list:
                print item
            req4 = raw_input("So, how can I help you today? ")
            if req4 == 'info':
                account_hafsa(updates, notifications)
            elif req4 == 'log out':
                time.sleep(2)
                print "You have been succesfully loged out."
        elif req4 == 'log out':
            time.sleep(2)
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password"
# End of account_hafsa
elif username == 'jack':
    if password == 'j':
        login_message(username, greating)
        req5 = raw_input("So, how can I help you today? ")
        if req5 == 'info':
            account_jack(updates, notifications)
        elif req5 == 'options':
            for item in list:
                print item
            req5 = raw_input("So, how can I help you today? ")
            if req5 == 'info':
                account_jack(updates, notifications)
            elif req5 == 'log out':
                time.sleep(2)
                print "You have been succesfully loged out."
        elif req5 == 'log out':
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password"
