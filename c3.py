# x= 10
# y= "hi"
# z= "hello"
# print(y)

# breakpoint()

# print (z)
# #click c to continue and n to next line q to quit/stop

# for i in range(10):
#     print ("i =",i)

#     if i == 5:
#         breakpoint()



# def debugger (a,b):
#     import pdb; pdb.set_trace()
#     result = a/b
#     return result

# print (debugger(5,10))

def square(n):
    """takes in a number n, returns the square of a"""
    return n**2
print (square.__doc__)

numerator = 10
denominator = 1
#check condition for assertionerror
assert denominator !=0
#does division only if the denominator is not equal to 0
result = numerator
print (result)


def add(x,y):
    """add function"""
    return x + y

def subtract(x,y):
    """subtract function"""
    return x - y

def multiply(x,y):
    """multiply function"""
    return x * y

def divide(x,y):
    """divide function"""
    if y==0:
        raise ValueError ("cannot divide by zero")
    return x/y


import unittest
import calc
class TestCalc(unittest,Testcase):
    def test_add(self): #changing the vcariable to add test wont run any test
        result = calc.add(10,5)
        self.assertEqual(result,15)#cahnge value from 15 to 14
a = 10
b = 5
add (10,5)
result = 10 + 5
result == 15