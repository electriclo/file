#print lines in reverse
with open ("file2.txt","r") as file:
     lines = file.readlines()
print (lines)
for sites in reversed(lines):
    print (sites.strip())
file.close()

#print length
print ("this program reads the lines of a file and prints the length of each string")
with open("file2.txt","r") as file:
    for line in file:
        print (len(line))
file.close

#print 1 to 10
with open("file3.txt", "w" ) as optfile:
  for i in range(1, 11):
   optfile.write(str(i)+ "\n")
optfile.close()

#error practice


#try:
   # 5/0
#except ZeroDivisionError:
   # print ("you cannot divide by 0")

a = int (input("enter the first number"))
b = int (input("enter the second number"))
try:
    result = a/b
    print ("result=",result)
except:
    print ("exception handled")

print ("end of program")

with open("FileEx5.txt", "w" ) as optfile:
  for i in range(1, 11):
   optfile.write(str(i)+ "\n")
optfile.close()


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


import sys 
try:
    num =int (input("enter the numerator"))
    den = int (input("enter the denominator"))
    result = num / den;
    print ("result=",result)
except ValueError:
    print ("invalid input")
except ZeroDivisionError:
    print ("divide by zero error")

print ("end of program")


try:
    print ("eneter the marks")
    marks=int(input())

    if marks <0 or marks >100:
        raise ValueError
except ValueError:
    print ("input out of range")