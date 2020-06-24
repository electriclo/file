import random
print ("the cpin flip game\n")

heads = 0
tails = 0
count = 0

while count < 2:
    coin = random.randrange(2)

    if coin == 0:
        heads = heads + 1
    else:
        tails = tails + 1

    count += 1

print ("heads: ",heads)
print ("tails: ",tails)


input("\npress enter to exit")