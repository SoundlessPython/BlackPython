import time
name = raw_input("What is your name : ")
time.sleep(1)
while name == 'david':
    print "Before I can put you through to the main system, I need to ask a few questions."
    time.sleep(2)
    input2 = raw_input("Please enter your passcode : ")
    list = ['status', 'nothing', 'help']
    print "You have three options to choose from:"
    print list[0]
    time.sleep(1)
    print list[1]
    time.sleep(1)
    print list[2]
while name != 'david':
    print "Sorry, I can't find your name on my database"
    name = raw_input("What is your name : ")
