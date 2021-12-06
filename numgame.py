import random
import time

def numGame():

    #obviously stated, but get user preferred highest possible guess.
    highest = int(input("What should be the highest possible number?\nPositive whole numbers only: "))

    #Set a random winning number
    winningNum = random.randint(1, highest)


    guess = int(input(f"\nEnter a number between 1 and {highest}.\nPositive whole numbers only: "))


    while winningNum != guess:

        #Guess less than set limit
        if guess < winningNum:
            print("\nToo low, try again!")
            guess = int(input(f"Enter a number between 1 and {highest}.\nPositive whole numbers only: "))


        #Guess greater than set limit, just had some fun here.
        elif guess > highest:
            time.sleep(1)
            
            print("\n...")
            time.sleep(1.5)

            print (f"That's higher than {highest}")
            time.sleep(2)

            print(f"You literally JUST entered {highest} as the highest possible number")
            time.sleep(1.5)

            guess = int(input(f"\nNow try again to enter a number between 1 and {highest}.: "))

            if guess > highest:
                print("\nbro.")
                time.sleep(2)
    
                print("It really isn't that hard.\n")
                time.sleep(1.5)

                guess = int(input(f"a number between 1 and {highest}.: "))

                if guess > highest:
                    guess = int(input("\nIm giving you one last chance: "))

                    if guess > highest:
                        print("K.")
                        time.sleep(1)
                        quit()

            elif guess > winningNum:
                print("\nToo high, try again!")
                guess = int(input(f"Enter a number between 1 and {highest}. \nPositive whole numbers only: "))

    print("\nNice job! You guessed correctly!")

    playing = (input("\nDo you want to play again? Y/N:  "))

    if playing == "y" or playing == "Y":
        print("Starting over!")
        time.sleep(0.4)
        numGame()

    else: 
        print ("\nThanks for playing!")
        time.sleep(1.2)

numGame()