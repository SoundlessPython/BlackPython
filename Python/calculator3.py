# Define our function
def calculate():
    #Define again() function to ask user if they want to calculate again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')   
    operation = input(
'''
Please type in the math operation you would like to complete
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

# Addition
if operation == '+':
   print('{} + {} = '.format(number_1, number_2))
   print(number_1 + number_2)

# Subtraction
elif operation == '-':
     print('{} - {} = '.format(number_1, number_2))
     print(number_1 - number_2)

# Multiplication
elif operation == '*':
     print('{} * {} = '.format(number_1, number_2))
     print(numbrt_1 * number_2)
# Division
elif operation == '/':
     print('{} / {} = '.format(number_1, number_2))
     print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')

    calculate()
