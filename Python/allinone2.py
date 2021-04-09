from sys import argv

#script, first, second, third = argv

#print "The script is called :", script
#print "Your first variable is: ", first
#print "Your second variable is: ", second
#print "Your third variable is: ", third

#import sys
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

