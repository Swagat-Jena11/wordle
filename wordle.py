# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:24:28 2023

@author: swagat
"""
import random
from termcolor import colored
import sys

#Create Dictionary
file1 = open('word.txt','r')
st = file1.readlines()
for i in range(0,len(st)):
   st[i] = (st[i].strip()).upper()

word = random.choice(st)

#Welcome
print('You are playing ', end='')
print(colored('WORDLE','green', attrs=['bold']))

#Tutorial
print('Tutorial:')
print('1. Guess a 5 letter word. You can only enter 5 letter words. The words must be part of the dictionary.')
print('2. The game will give you hints after each guess.')
print('3. If your input letter turns', colored('YELLOW','yellow',attrs=['bold']), ': letter is present in the word, but different position')
print('4. If your input letter turns', colored('GREEN','green',attrs=['bold']), ': letter is present in the word, at correct position')
print('5. If letter remains white, the letter is not present in the word.')
print('6. Number of attempts is 6.')
print(colored('Good Luck!','magenta',attrs=['bold']))


#Take Guesses
attempts=0
print('Start Guess: ')
while(attempts<6):
    guess = input().upper()
    
    # overwrite the last line in the console
    sys.stdout.write('\x1b[1A\r')
    sys.stdout.write('\x1b[2k\r')

    print('     \r', end='')

    #Guessed word must be part of Dictionary
    if(not(guess in st)):
        continue
    
    #temporary word used in check algorithm
    checker=word

    correct=0
    for i in range(5):
        if(guess[i]==checker[i]):
            print(colored(guess[i],'green',attrs=['bold']),end=' ')
            checker=checker[:i]+' '+checker[i+1:]
            correct+=1
        elif(guess[i] in checker and not(guess[i] in guess[i+1:])):
            print(colored(guess[i],'yellow',attrs=['bold']),end=' ')
        else:
            print(guess[i],end=' ')
    print()
    if(correct==5):
        break
    attempts+=1
    
if(attempts<6):
    print(f'Congratulations. You completed the guess in {attempts+1} attempts')
else:
    print(colored(word,'red',attrs=['bold']))



