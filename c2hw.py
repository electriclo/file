#the error will be nameerror.
#i have to write the variable in this file for it to print.

try:
    value = my_dict["d"]
except:
    KeyError:
    print ("that key doesnt exist")

print ("end of program")


#question 2
my_list = [1,2,3,4,5]
try:
    my_list
except:
    NameError
    print ("exception handled")

print ("end of program")
#?