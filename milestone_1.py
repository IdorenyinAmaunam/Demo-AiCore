import random
import string

word_list = ["apple", "banana", "cucumber", "carrot", "orange"]

word = random.choice(word_list)

guess = input("Please, Enter a single character: ")

if len(guess) == 1 and (guess.isalpha()):
    print("Good guess")
else:
    print("Oops!")

type(word_list)
print(type)
print(word_list)
print(word)
