# As I have not created a new program in quite a while, I decided today is the day I get back to work.

def add(x, y):
	return x + y
# adds x and y

def subtract(x, y):
	return x - y
# subtracts x from y

def multiply(x, y):
	return x * y
# multiplys x and y

def divide(x, y):
	return x / y
# divides x by y

print "Select an operation."
print """
      1 : ADD
      2 : SUBTRACT
      3 : MULTIPLY
      4 : DIVIDE
      """

choice = input("Which one do you choose? ")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

if choice == '1':
	print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
	print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
	print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
	print(num1, "/", num2, "=", divide(num1,num2))
