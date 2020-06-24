# from random import choice

# word = choice(["code","club"])

# out =""

# for letter in word:
#     out = out + "_"

# print ("guess a letter in the word",out)

from random import choice

word = choice(["code","club"])

out =""

for letter in word:
    out = out + "_"

print ("guess a letter in the word, then press enter")

guess = input()

if guess in word:
    print ("yay")

else:
    print ("no")