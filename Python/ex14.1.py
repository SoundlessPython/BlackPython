from sys import argv
script, user_name = argv
prompt = '> '
print
print
print
likes
"Hi %s, I'm the %s script." % (user_name, script)
"I'd like to ask you a few questions."
"Do you like me %s?" % user_name
= raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
