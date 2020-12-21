python = "A programing language "
python2 = "A deadly snake"

list = ['boy', 'girl', 'mum', 'dad']
for item in list:
    print item
import time

#I think I am getting the hang of python listsself.
a = raw_input("Which one of them are you?: ")
if a == 'boy':
    print "Hi boy"
    print list[:1]
elif a == 'girl':
    print "Go away"
    print list[:2]
elif a == 'mum':
    print "t"
    print list[:3]
elif a == 'dad':
    print "OH, so you are back."
    print list[:4]
else:
    print "I said chose one of the four options that I gave you!!!"
print "When a regular person hears the word python, they think of %s" % python2
time.sleep(3)
print "But when a programmer hears the word python, they think of %s" % python
