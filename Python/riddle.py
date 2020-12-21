import time
print "Welcome stranger, to this game."
name = raw_input("State your name, stranger : ")
print "Ok then, lets get started %s" % name

print "You walk into a room and see two doors."
time.sleep(1)
choice = raw_input("Which do you choose, room A or room B : ")

if choice == 'A':
	time.sleep(1)
	print ""