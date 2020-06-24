# import random
# print (random.randint(1,100))


import random 
#this generates the random number
num = random.randint (1,100)
#random number is between 1 and 100
while True:
    #while the number is between 1 and 100, which is always
    print ("guess a number between 1 and 100")

    guess = input()
    #the number you type is the guess
    i = int(guess)
    if i == num:
        print ("you are right")
    elif i < num:
        print ("guess higher")
    elif i > num:
        print (" guess lower")


    yes = input(y)
    if yes = True:
        
