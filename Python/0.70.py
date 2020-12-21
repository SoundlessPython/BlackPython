username = raw_input("Please enter your username: ")
password = raw_input("Please enter your password: ")
options = ['1', '2', '3',]
def account_umar():
    print "Umar"
if username == 'umar':
    if password == 'umar2':
        print "Hi %s" % username
        for item in options:
            print item
        choice = raw_input("Which number do you choose? ")
        if choice == '1':
            print "Wrong"
        elif choice == '2':
            print "Close but not quite right."
        elif choice == '3':
            print "Spot on bro." 
