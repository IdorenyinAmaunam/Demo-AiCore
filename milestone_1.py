from ctypes.wintypes import WORD
import random
import string

class Hangman:

    word_list = ["apple", "banana", "cucumber", "carrot", "orange"]

    word = random.choice(word_list)



    def accept_input(self):
        guess = input("Please, Enter a single character: ")

        if len(guess) == 1 and (guess.isalpha()):
            print("Good guess")
            
        else:
            print("Oops!")

        return guess

    def show_display(self,guess):
        print(word)

        return word


hangman_obj = Hangman()

hangman_obj.accept_input()
hangman_obj.show_display()

