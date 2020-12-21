import time
J = 31
F = 28
M = 31
A = 30
Ma = 31
Ju = 30
JU = 31
Au = 31
S = 30
O = 31
N = 30
D = 31

string = "Hey, this is a test of how len works in python."
print string
#time.sleep(3)
# print "String Length:", len(string)
age = int(input("How old are you : "))
birthday = raw_input("What day is your birthday : ")
day = 365 - birthday
month = raw_input("In what month does that day fall : ")
if month == 31:
	print day
print "You will be", age + 1 ,"in a year."