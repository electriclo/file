import random
print("The coin flip game \n")


count=0
headscount=0
tailscount=0
print("hit x to exit")
while True:
    heads=0
    tails=0
    coin = random.randrange(2)
    if coin == 0:
        heads+=1
        headscount+=1
    else:
        tails+=1
        tailscount+=1
    count+=1
    guess=input("Type heads or tails: ")
    if guess=="heads" and heads==1:
        print("You win!")
    elif guess=="tails" and tails==1:
        print("You win!")
    elif guess=="heads" and heads==0:
        print("Coin landed on tails, better luck next time.")
    elif guess=="tails" and tails==0:
        print("Coin landed on heads, better luck next time.")
    elif guess=="x":
        print("Game over :(")
        print("You played ", count, " times")
        print("heads:",headscount,"\ntails:",tailscount)
        break