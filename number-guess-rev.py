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