# So this is my first attempt at making a functioning game.
import time
a = 'fox'
b = 'dog'
c = 'cat'
d = raw_input("> ")
time.sleep(2)
print "Don't like the suspence, huh."
time.sleep(2)
if d == a:
    print "Not bad %s is = to %s, good choice." % (a, d)
    print "You win."
elif d == b:
    print "Sorry, that is not the answer I was looking for."
    print "Try again."
elif d == c:
    print "Close, but not the right answer."
    print "You loose, sucker."
else:
    print "Sorry, too bad bro."
print "If you typed the wrong answer, please try again."
print "So how was the game?"
print "Was it good?"
print "I hope so"
if d == 1916918112:
    print "Wow, you know the access code."
    print "Who would have guessed."
