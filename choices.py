# Step 1: Pick a word
from random import choice

word = choice(["code", "club"])

print(word)
# #Step 2: Guess a letter
# from random import choice

# word = choice(["code", "club"])

# out = ""

# for letter in word:
#     out = out + "_"

# print("Guess a letter in the word:", out)


# Letting user input a letter
from random import choice

word = choice(["code", "club"])

out = ""

for letter in word:
    out = out + "_"

print("Guess a letter in the word, then press enter:", out)

guess = input()

if guess in word:
    print("Yay")
else:
    print("Nope")