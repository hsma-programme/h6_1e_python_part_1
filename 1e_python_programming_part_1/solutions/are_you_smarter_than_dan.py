#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:52:35 2019

@author: dan
"""

# import the random library
import random

# Set high score to 0, and continue play to True
high_score = 0
continue_play = True

# Put all the game logic in a while loop, that keeps going until continue_play
# becomes false
while continue_play == True:
    # Print welcome message
    print ("Welcome to the game.  I'm thinking of a number between 1 and 100.")
    print ("Can you guess what number I'm thinking of?")
    print ()
    
    # Get the computer to pick a random number between 1 and 100
    computer_number = random.randint(1,100)
    
    # Set initial game parameters (reset for each game)
    number_of_guesses = 10
    correctly_guessed = False
    score = 1000
    list_of_guesses = []
    
    # Loop for player guesses (a single go of the game)
    for i in range(number_of_guesses):
        # Ask user to make a guess
        print (f"This is guess number {i+1}")
        user_guess = int(input("INPUT YOUR GUESS : "))
        
        # Add the guess to the list of guesses
        list_of_guesses.append(user_guess)
            
        # If the user guesses correctly, print the score and the list of
        # guesses, update that the user guessed correctly, and break from the 
        # for loop (end the current go)
        if user_guess == computer_number:
            print ("Correct!  Well done.")
            print (f"You scored {score}")
            print (f"Your guesses : {list_of_guesses}")
            correctly_guessed = True
            break
        # if the user guess is less than the number, say they are too low and
        # deduct 100 from the score
        elif user_guess < computer_number:
            print ("Too low.")
            score -= 100
        # if the user guess is higher than the number, say they are too high
        # and deducated 100 from the score
        else:
            print ("Too high.")
            score -= 100
    
    # If the user didn't manage to guess correctly, tell them they lost along
    # with what the number actually was, and a list of their guesses.
    if correctly_guessed == False:
        print (f"You lose.  The number was {computer_number}.")
        print (f"Your guesses : {list_of_guesses}")
        
    # If they beat the previous high score, print a message and update the high
    # score
    if score > high_score:
        print (f"NEW HIGH SCORE - {score}")
        high_score = score
        
    # Ask if the user wants to play again.  If they type anything other than Y
    # then set continue_play to False, thereby exiting the while loop and
    # terminating the program.
    play_again_choice = input("Type Y to play again : ")
    
    if play_again_choice != "Y":
        continue_play = False
        
