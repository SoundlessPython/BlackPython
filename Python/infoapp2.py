import time
def acc1():
    print """
     Name : Umar
     Age : 16
     Food : cake
     Drink : Water
     """
username = raw_input("Username : ")
while username != 'Umar':
	print "Sorry, Wrong username."
	username = raw_input("Please try again : ")
password = raw_input("Password : ")
while password != '3333':
	print "Sorry, Wrong password."
	password = raw_input("Please try again : ")
print "Hi, Umar. You have succesfully loged on"
acc1()