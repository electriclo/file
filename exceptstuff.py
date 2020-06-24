#a = 5
#b = 0
#result = a/b

#Try and Except for ZeroDivError
try:
    5/0
except ZeroDivisionError:
    print("You cannot divide by zero!")

#Try and Except handling program
a = int ( input('Enter the first number ') )
b = int ( input('Enter the second number ') )

try:
    res = a/b
    print('result =',res)
except:
    print('Exception Handled ')

print('End of Program')

#Nested Try and Introducing Value Error
try:
    num = int ( input('Enter the numerator ') )
    den = int ( input('Enter the denominator ') )
    try:
        result = num/den;
        print('Result =',result)
    except:
        print('Divide by Zero Error')
except:
    print('Invalid Input')

print('End of program')

#To know type of Exception

import sys
a = int ( input('Enter the first number ') )
b = int ( input('Enter the second number ') )

try:
    res = a/b
    print('result =',res)
except:
    print('Exception Handled ')
    print("Oops!",sys.exc_info[0],"occured.")

print('End of Program')
