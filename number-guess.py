from random import randint
def startgame(): 

    guessamount = input("How large do you want the range of numbers to pick be?(Limit is 500): ")
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
                print ("You suck at this game. The answer is lower than " + str(guess))
            else:
                print ("You suck at this game. The answer is higher than " + str(guess))

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
run_once = 0
while 1:
    if run_once == 0:
        startgame()
        run_once = 1