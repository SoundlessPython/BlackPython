#2 a mapping
#1 a collection of code
def function1():
    print("Ahhh")
    print("Ahhh 2")
print "This is out of the function."
function1()
def function2(x):
    return 2 * x
a = function2(3)
#return value of output
print a
b = function2(4)
print b
c = function2(10)
print c
def function3(x, y):
    return x * y
e = function3(2, 2)
print e
def function4(x):
    print x
    print "Still in this function."
    return 5 * x
f = function4(2)
print f
