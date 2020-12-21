#!/usr/bin/python


def checkName(name):
    checkName = input("Is your name " + name + "? ")

    if checkName.lowwer() == "Umar":
        print "Hello,", name
    else:
        print "We're sorry about that."

checkName("Umar")
