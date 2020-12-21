import getpass
key = getpass.getpass('Please Enter The Key : ')

while key != '?1$6':
	print "Wrong key."
	key = getpass.getpass('Please Enter The Key : ')

if key == '?1$6':
	print "Hurayy, your in!!!"
