from random import randint
def twoplayer_switch(): 

    guessamount = input("How large do you want the range of numbers to pick be?(Limit is 500): ")
    if int(guessamount) > 500:
        guessamount = 500
    turn_switch = 1

    answer = randint(int(1), int(guessamount))
    attempts = 5

    while attempts != 0 and attempts != 6:
        guess = input(f"Player {turn_switch} Guess a number between 0-" + str(guessamount) + ": ")

        if answer == int(guess):
            attempts = 6
        else:

            if int(guess) > int(answer):
                print (f"Player {turn_switch} You suck at this game. The answer is lower than " + str(guess))
                if turn_switch == 1:
                    turn_switch = 2
                else:
                    turn_switch = 1
            else:
                print (f"Player {turn_switch} You suck at this game. The answer is higher than " + str(guess))
                if turn_switch == 1:
                    turn_switch = 2
                else:
                    turn_switch = 1

    if answer == int(guess) and attempts != 5:
        print(f"Player {turn_switch} won the game! The answer was " + str(answer))
        playagain = input("Would you like to play again?(Y/N): ")
        if playagain == "Y" or playagain == "y":
            twoplayer_switch()
        else:
            exit()
run_once = 0
while 1:
    if run_once == 0:
        twoplayer_switch()
        run_once = 1