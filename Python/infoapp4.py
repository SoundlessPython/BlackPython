updates = "nothing new"
notifications = "I don't know what this does."
username = raw_input("Enter username: ")

password = raw_input("Enter password: ")
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
def login_message(username, greating):
    print("Hello, %s ,I hope you enjoy your visit.") % username
while username == 'ac100':
    while password == '10100':
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
                
                print "You have been succesfully loged out."
        elif req == 'log out':
            
            print "You have been succesfully loged out."
    else:
        print "Sorry, wrong username or password."
