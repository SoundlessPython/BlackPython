 
 #!/usr/bin/python
import time
options = ['Fox', 'Dog', 'Cat']
print "You have three options to choose from."
time.sleep(2)
for item in options:
	print item
time.sleep(1)
a = raw_input("Which one do you choose: ")
time.sleep(2)
print "I will try to guess what you typed."
time.sleep(2)
print "You type Fox, Dog or Cat "
time.sleep(2)
print "I know I am right." 