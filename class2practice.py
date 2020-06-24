# try:
#     print ("enter the marks")
#     marks=int(input())

#     if marks <0 or marks >100:
#         raise ValueError
# except ValueError:
#     print ("input out of range")

try:
    a =int(input("enter the first number"))
    b =int(input("enter the second number"))

    res = a/b
    print ("res =",res)
except (ValueError,TypeError):
    print ("invalid input error")
except ZeroDivisionError:
    print ("divide by zero error")
finally:
    print ("this code will run no matter what")
print("end of program")