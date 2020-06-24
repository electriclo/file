x = "awesome"

def myfunc ():
    x = "fantastic"
    print ("python is " + x)

myfunc()


print ("python is " + x)


def f():
    s ="python"
    print (s)
s = "i love python"
print ("the string: + s")
f()

def gamenumber():
    while True:
        difficulty = input("type e for easy, m for medium, h for hard")
        difficulty.lower()

        if difficulty == "e":
            return random.randint(1,20)

        elif difficulty == "m":
            return random.randint(1,50)

        elif difficulty == "h":
            return random.randint(1,100)


        else:
            print ("incorrect input")



def numberguessgame():
    number = gamenumber()
    while True:
        try:
            guess = int(input("your guess"))
            if number == guess:
                print ("correct guess")
                return numberguessgame() if input("press y to play again, any other key to exit").lower()== "y" else 0
            print ("too high" if number > guess else "too low")
        except ValueError:
            print ("must be an integer")


def main():
    numberguessgame()


main()