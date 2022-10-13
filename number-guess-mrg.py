from random import randint
import getpass

# Game starting
def startgame():
    gameselect = input("Which game would you like to play? (1p, 2p, rev): ")
    if gameselect == "1p":
        oneplayer()
    elif gameselect == "2p":
        twoplayer()
    elif gameselect == "rev":
        reverse()

#
# One player game
#

def oneplayer(): 

    guessamount = input("How large do you want the range of numbers to pick be?(Limit is 500): ")
    if int(guessamount) > 500:
        guessamount = 500

    answer = randint(int(1), int(guessamount))
    attempts = 5

    while attempts != 0 and attempts != 6:
        guess = input("Guess a number between 0-" + str(guessamount) + ": ")

        if answer == int(guess):
            attempts = 6
        else:
            attempts -= 1

            if int(guess) > int(answer):
                print ("Incorrect. The answer is lower than " + str(guess))
            else:
                print ("Incorrect. The answer is higher than " + str(guess))

    if answer == int(guess) and attempts != 5:
        print("You won the game! The answer was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()
    else:
        print("You ran out of attempts. The number was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()
#
# Two player game
#

def twoplayer(): 

    # Allows the user to select the range
    guessamount = input("How large do you want the range of numbers to pick be?(Limit is 500): ")
    if int(guessamount) >= int(500):
        guessamount = 500

    # Allows player 1 to select the answer for player 2 to guess
    answer = getpass.getpass("Player 1 select the answer (The answer will not show up while typing):")
    if int(answer) >= int(guessamount):
        answer = guessamount
    attempts = 5

    while attempts != 0:
        guess = input("Player 2 Guess a number between 0-" + str(guessamount) + ": ")

        if int(answer) == int(guess):
            attempts = 0
        else:
            attempts -= 1

            if int(guess) > int(answer):
                print ("Player 2, Incorrect. The answer is lower than " + str(guess))
            else:
                print ("Player 2, Incorrect. The answer is higher than " + str(guess))

    if int(answer) == int(guess):
        print("Player 2, You won the game! The answer was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()
    else:
        print("Player 2, You ran out of attempts. The number was " + str(answer) + " Player 1 wins!!")
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()

#
# Reverse Game
#

from random import randint
def reverse(): 

    guessamount = input("How large do you want the range of numbers to pick be?(Limit is 500): ")
    if int(guessamount) >= 500:
        guessamount = 500

    answer = input("Select the number for the AI to guess: ")
    if int(answer) >= int(guessamount):
        answer = guessamount
    attempts = 5

    while attempts != 0 and attempts != 6:
        guess = randint(0, guessamount)

        if answer == int(guess):
            attempts = 6
        else:
            attempts -= 1

            if int(guess) > int(answer):
                print ("The AI's guess is lower than " + str(guess))
            else:
                print ("The AI's guess is higher than " + str(guess))

    if answer == int(guess) and attempts != 5:
        print("The AI won the game, you lose! The answer was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()
    else:
        print("The AI ran out of attempts, you win! the number was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            startgame()
        else:
            exit()

#
# Setup Game
#

startgame()