print "You enter a cave, and you see a dragon sleeping"
print "You have 4 choices,"
things = ['a', 'b', 'c', 'd']
for item in things:
    print item
choice = raw_input("Which one do you choose? ")
if choice == 'a':
    print "You chose to sneek past the dragon"
elif choice == 'b':
    print "You chose to wake the dragon up"
    print "Great, the dragon bits your head off."
elif choice == 'c':
    print "You chose to leave the cave ASAP."
elif choice == 'd':
    print "You chose not to move; afraid of waking the dragon."
