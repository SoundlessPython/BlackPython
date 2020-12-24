print "Marry had a littlr lamb. "
print "Its fleece was white as %s." % 'snow'
print "And weverywhere that Marry went."
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.", 
	"But it didn't sing.", 
	"So I said goodnight."
	)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

grades = "\n\nP\nM\nD\n"
# ' \" ' is used to move the next item in the string over to a new line.

print "These are the BTEC grades: ", grades

print "He is 7'2\" tall."
# ' \" ' is used to include quotation marks in a string.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t*Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "How old are you? ", 
age = raw_input()
print "How tall are you? (in feet and inches) ",
height = raw_input()
print "How much do you weigh? (in Kgs) ",
weight = raw_input()

print "So you are %r old, %r tall and %r Kgs heavy." % (age, height, weight)