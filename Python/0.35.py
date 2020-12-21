# This is my attempt at creating a program that logs my runs, in order to be more organised
# This line of code prompts the user fo a date on which a run was compleated
# If the date entered cannot be fount the file will not find anything.
a = input("Please enter the date of your run: ")
import time
time.sleep(1)
print "OK, let me just bring up the details of that run"
time.sleep(2)
print "This may take a few seconds"
time.sleep(1)
print "..."
time.sleep(5)
if a == 130318:

    print'''
    Time compleated: 14:45

    How you felt: Great

    Date: 130318
         '''
elif a == 150318:
    print '''
    time compleated: 17:30

    How you felt: great at the start, but not so much at the end

    Date: 150318
         '''
else:
    print "Sorry, I can't find the date", a,"on my database."
    time.sleep(2)
    print "Please try again using a diffrent date."
