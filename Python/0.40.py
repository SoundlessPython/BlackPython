a = raw_input("Please enter a day: ")
import time
time.sleep(2)
print "Let me just bring up the details."
time.sleep(4)
print "Acording to my information:"
if a == 'monday':

    print "You should focus on biology as it is due today."
    time.sleep(2)
    print "However, if the time is past 9 o'clock then you shuld be working on math and chemistry."
elif a == 'tuesday':
    print "You should focus on math and chemistry today."
