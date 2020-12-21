def acc1():
	print """
	Name : B
	Age : 7
	Note : go to sleep
	"""

username = raw_input("Username: ")
password = raw_input("Password: ")

if username == 'Mary':
	if password == '1111':
		acc1()



elif username != 'Mary':
	reusername = raw_input("Not Mary? Please enter your username: ")