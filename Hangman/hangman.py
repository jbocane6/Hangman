#!/usr/bin/python3
import os
import random
from words import word_list

def paint(word, error):
    os.system('clear')
    attempts = 6 - error
    print("Remaining attempts: {:d}".format(attempts))
    for i in range(0,error):
        print("{}".format(muñeco[i]))
    print("\n{}\n".format(word))

guess = random.choice(word_list)
lines = len(guess)
error = 0
word = ""
muñeco = " +---+", " |   |", " O   |", "/|\  |", "/ \  |", "     |\n========="

for i in range(0,lines):
    word = word + "_"
paint(word, error)
print("")

while (error < 6):
    while True:
        paint(word, error)
        letter= input("Please, input letter: ")
        if (len(letter) == 1):
            break
    
    if (guess.find(letter) != -1):
        for i in range(0,lines):
            if (letter == guess[i]):
                new = list(word)
                new[i] = letter
                word = ''.join(new)
            paint(word, error)
        if (word == guess):
            print("You Win")
            exit(0)
    else:
        error = error + 1
        paint(word, error)

print("The word was: {}\nYou Lost".format(guess))
exit(1)
