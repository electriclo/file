import random
print("rps \n")


count=0
rockcount=0
papercount=0
scissorscount=0
print("hit x to exit")
while True:
    rock=0
    paper=0
    scissors=0
    cpu = random.randrange(3)
    if cpu == 0:
        rock+=1
        rockcount+=1
    elif cpu == 0:
        paper+=1
        papercount+=1
    else:
        scissors+=1
        scissorscount+=1
    cpu+=1
    playerinput=input("Type rock,paper,or scissors.")
    if playerinput=="rock" and cpu == rock:
        print ("rock vs rock")
        print("tie")
    elif playerinput=="rock" and cpu == paper:
        print ("rock vs paper")
        print(" cpu wins")
    elif playerinput=="rock" and cpu == scissors:
        print ("rock vs scissors")
        print ("you win")

    elif playerinput=="paper" and cpu == paper:
        print ("paper vs paper")
        print("tie")
    elif playerinput=="paper" and cpu == scissors:
        print ("paper vs scissors")
        print(" cpu wins")
    elif playerinput=="paper" and cpu == rock:
        print ("paper vs rock")
        print ("you win")

    elif playerinput=="scissors" and cpu == scissors:
        print ("scissors vs scissors")
        print("tie")
    elif playerinput=="scissors" and cpu == rock:
        print ("scissors vs rock")
        print(" cpu wins")
    elif playerinput=="scissors" and cpu == paper:
        print ("scissors vs paper")
        print ("you win")
    elif playerinput=="x":
        print("Game over")
        print("You played ", count, " times")
        break