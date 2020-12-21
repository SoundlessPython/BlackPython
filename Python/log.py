import time
key = input("Please enter the sipher key: ")
if key == 9999:
    a = input("Please type a date: ")
    print "OK, just let me bring up the details."
    time.sleep(2)
    print "This may take a few seconds."
    time.sleep(2)
    print "..."
    time.sleep(4)
    if a == 110318:
        print "Hi, this is the first version of LogBlog"
        time.sleep(3)
        print "This is a systen for keeping daily entries, like a diary just more complex"
        time.sleep(3)
        print "This system might turn out to be useful to sombode with some experience in coding and would like to encrypt their entries."
        time.sleep(4)
        print "Today was quite uneventfull, as nothing really interesting happened."
        time.sleep(3)
        print "I did however have an amazing run today."
        time.sleep(3)
        print "Other than that, I have greatly improved in python programing."
        time.sleep(3)
        print "So much so that I have allready started creating programs to help make my life more organised"
        time.sleep(3)
        print "Like this program/log/blog/jornal/what ever you want to call it."
    elif a == 120318:
        print "Next day is allready here."
        time.sleep(2)
        print "On todays agenda:"
        time.sleep(2)
        print "Perfecting LogBlog"
        time.sleep(1)
        print "Tuition at 4pm"
        time.sleep(1)
        print "And finally, some LPTHW "
        time.sleep(3)
        print "Sigh, I have a physics test today and I am not looking foward to it. "
        time.sleep(2)
        print "Hopefully I will do well in this test."
        time.sleep(2)
        print "As for LogBlog, it is improving steadilly and soon it will be a part of everyday life MUHAHAHAHAHAHA."
        time.sleep(2)
        print "I still can't believe that I am this good at programming, Hopefully soon I will be a world renound programmer/developer."
        time.sleep(2)
        print "Well, now I will boot down my workstation because I am off to tuition to take a test."
        print "Good bye, python........."
    elif a == 130318:
        print "Third day of using LogBlog and I still haven't thought of a good name, as LogBlog sounds incompleate."
        time.sleep(2)
        print "I could actually get used to clogging my daily activities on my secure server."
        time.sleep(2)
        print "See, tis is what is ment by automating the boring stuff with python."
        time.sleep(2)
        print "Like, seriously who has time to be looking in a diary for an entry when you can just type in the date and BAMM, Bob's your uncle."
    elif a == 140318:
        print "Nothing to write today."
    elif a == 150318:
        print "Today I hope I can find time to go for a run"
        time.sleep(2)
        print "Ok, so I managed to get a run in and for some reason I felt great at the start of the run, but not so great at the end."
        time.sleep(3)
        print "Never the less, I will strive to become a better runner and some day be able to run a marathon."
        time.sleep(3)
        print "As for python, I seem to be getting more familiar with the diffrent commands."
        time.sleep(2)
        print "I keep learning new commands, such as time.sleep() which delays a line from being read by python."
        time.sleep(3)
    elif a == 160318:
        print "So today is the sixth day of LogBlog, and it's going fine."
        time.sleep(2)
        print "I think I am going to change this programs name to (Hacker's Log)"
        time.sleep(2)
        print "As for my programming, I think I would be able to call myself an expert soon."
    elif a == 200318:
        print "So, it has been a few days since I last wrote."
        time.sleep(2)
        print "Weirdly enough, I have been coding python for about 5 weeks and I think I am getting it."
    elif a == 300318:
        print "Ok, so I have not logged on for a few weeks"
    elif a == 10418:
        print "ooo"
    elif a == 110918:
        print "So it has been about 6 months since I last logged on to log."
    else:
        time.sleep(3)
        print "...."
        time.sleep(2)
        print "Sorry,I can not find the key", a, "on my database. "
        time.sleep(1)
        print "Please run me again using a difrent entry key."
else:
    print "...."
    print "Sorry, ", key, "is the wrong key"
    print "If by any chance you are trying to acsess information "
    print "that does not belong to you, I will destroy you."
