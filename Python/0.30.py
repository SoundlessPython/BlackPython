a = int(input("Please type your age: "))
b = int(input("Please type how many weeks you've been running for: "))
c = int(input("How long is yor average run: "))
import time
print "Calculating ..."
time.sleep(1)
print "This may take a few seconds ...."
time.sleep(4)
if b * c / 20 > 30:
    print "Acording to your age and your running experience you should be running three 30 min runs a week, or 9 miles per week"
elif b * c / 20 < 30:
    print ""
