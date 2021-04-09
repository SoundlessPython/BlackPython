result = ""
message = ""
choice = "6"
password = raw_input("Plese Enter The Passwprd >>>   ")

if password == "2021":
	while choice != 0:
		choice = input("\nDO you want to encrypt or decrypt?\nEnter 1 to encrypt, 2 to decrypt and 0 to exit the program. ")

		if choice == "1":
			message = input("\nEnter Message for encryption >  ")
			for i in range(0, len(message)):
				result = result + chr(ord(message[i]) - 2)

			print(result + '\n\n')
			result = ""

		elif choice == "2":
			message = input("\nEnter the message you want to decrypt > ")
			for i in range(0, len(message)):
				result = result + chr(ord(message[i]) + 2)

			print(result + '\n\n')
			result = ""

		elif choice == "0":
			print("Goodbye")

		elif choice != "0":
			print("You have entered an invalid input. Please try again. \n\n") 

elif password != "2021":
	print("Sorry, Wrong pasword.")
#Test encryption message:
#	"Today is Monday 21st of August 2021, the mission has been a failure and we were unable to retrieve the wild yetti. 
#	The men are tired and we are out of supplies. please send help! "





