def Umar():
    print "This is a test function."
    print "Please ignore anything it says."

def Sulaiman():
    print "This is a slightly more sophisticated function."
    print "Functions are actually quite usefull."
    print "The code is 'goo to sleep' "

def Laptop():
    print """
    So my plans to buy a new laptop are going great and I plan on
    getting the laptop
    by Eid Al Adhaa.
    The price I found just happens to be 649 pounds which is an absoluite bargen
    compered to the original price of 829 Quid, which is just out of my price
    range.
    """
a = raw_input("Please enter a number: ")

if a == '8888':
    Umar()
elif a == '7777':
    print "You have reached the laptop helpline......."
    Laptop()
else:
    Sulaiman()
    print "Sorry, Wrong number."
