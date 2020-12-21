import time
updates = "nothing new"
notifications = "nothing new"
name = raw_input("What is your name? ")
time.sleep(1)
password = raw_input("Master Key : ")
time.sleep(1)
print "Checking "
time.sleep(1)
print "."
time.sleep(1)
print "."
time.sleep(1)
print "."


list = ["     Apple", "     samsung", "     Huawei", "     Oneplus", "     HTC", "     Nokia", "     Motorola", ]

def g_m(updates, notifications):
	print("Hello, %s, I hope you enjoy your visit. ") % name
	for item in list:
		print item
	print "Updates: "


def apple(updates, notifications):
	print"""
	Date Established: 1st April 1976
	CEO: Tim Cook
	Worth: $1,000,000,000,000
	Global HQ: Cupertino, California, United States
	"""  
	print "Updates:"   

def samsung(updates, notifications):
	print"""
    Date Established: 1st March 1938
	CEOs: Ki Nam Kim, Hyun Suk Kim, and Dong Jin Koh
    Worth: $326,000,000,000
    Global HQ: Seoul, South Korea
	"""
	print "Updates:"

def huawei(updates, notifications):
	print """
	Date Established: 15th September 1987
	CEO: Ren Zhengfei 
	Worth: $105,100,000,000
	Global HQ: Shenzhen, China
	"""
	print "Updates: "

def oneplus(updates, notifications):
	print """
	Date Established: 16th December 2013
	CEO: Pete Lau
	Worth: $1,400,000,000
	Global HQ: Shenzhen, China
	"""
	print "Updates: "

def htc(updates, notifications):
	print """
	Date Established: 15th May 1997
	CEO: Cher Wang
	Worth: $1,500,000,000
	Global HQ: Michigan, United States
	"""
	print "Updates: "

print g_m(updates, notifications)
if password == "4444" :
	req = raw_input("Which company are you interestrd in today? ")
	if req == "apple" :
		print apple(updates, notifications)

elif password  != "4444" : 
	print sorry you have the wrong key




