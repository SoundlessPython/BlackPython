

import os
import time
#Must Access this to continue.
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'Bob' and PassWord == 'rainbow123':
            time.sleep(1)
            print ("Login successful!")
            logged()

        else:
            print ("Password did not match!")

def logged():
    time.sleep(1)
    print ("Welcome to ----")

main()
