def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b


print "This is my attempt at doing math with functions!"

age = add(10, 6)
height =subtract(66, 2)
weight = multiply(70, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, iq: %d" % (age, height, weight, iq)
               
