from random import choice

word = choice(["code","club"])

chance = 10
guessed = []
wrong = []

while chance > 0:
    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter

        else:
            out = out + "_"

    if out == word:
    #    print ("you guessed",word)
        break 
    print ("guess the word:", out)
    print(chance,"chances left")
    guess = input()

    if guess in guessed or guess in wrong:
        print ("already guessed", guess)
    elif guess in word:
        print ("yay")
        guessed.append(guess)
    else:
        print ("nope")
        chance = chance - 1
        wrong.append(guess)
    print ()

if chance:
    print("You guessed", word)
else:
    print("You didn't get", word)
    # for letter in word:
    #     if letter in guessed:
    #         print (chance)

    #     elif letter not in guessed:
    #         chance = chance - 1
            


