my_name = 'Umar .S'
my_age = 16
my_hobby = 'reading'
my_height = 70
my_weight = 150
a = input("Please type a number: ")
if a == 8554:
    print "Let's talk about %s ." % my_name
    print "He is %d years old." % my_age
    print "His hobbies consit of %s and skateboarding, not to mention coading." % my_hobby
    print "He is %d inches tall." % my_height
    print "He wheighs %d pounds."
    print "If I add %d, %d and %d I get %d" % (my_age, my_height, my_weight,my_age + my_height + my_weight)
elif a == 2211:
    print "Sorry, this part of the code script is still in development."
    print "Please try again later..."
elif a < 20:
    print "Let's talk about %s " % my_name
    print ".......An error has ocoured.........."
    print "Sorry for any inconvenience.........."
else:
    print "Too bad, wrong number."
