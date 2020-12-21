import time
print "You have 4 choices."
phones = ['Galaxy s8', 'LG G6', 'Iphone 8', 'oneplus 5t']
print phones[0]
time.sleep(1)
print phones[1]
time.sleep(1)
print phones[2]
time.sleep(1)
print phones[3]
choice = raw_input("Out of the phones above, which do you choose?: ")
if choice == 'galaxy s8':
	print """
	pros: 
	18:9 aspect ratio
	USB type-c charger
	5.8 inch AMOLED display
	Snapdragon 835 chip
	4 GB RAM
	Android 7.0 
	12MP Camera 
	3000 mAh battery
	facial recognition
	"""
	print """
	cons:
	oddly placed fingerprint senssor
	Not much more to say
    """
elif choice == 'lg g6':
	print """
	pros:
	18:9 aspect ratio
	USB type-c charger
	5.7 inch IPS LCD display
	Snapdragon 821 chip
	4GB RAM
	Android 7.0
	13MP camera
	3300 mAh battery
	"""
	print """
	cons:
	"""

	