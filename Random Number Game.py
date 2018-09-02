import sys
import random
# Class and method for checking guesses
class CheckGuess:
    def Call(self):
                    # Check guesses
                if guess == 20:
                    # User message
                    print("You ran out of guesses")
                    # Exit program
                    exit()
# Set Value for while loop
userPassed = 0
# Range of random
intRange = 1000
# Declare random
answer = random.randint(1, 1000)
# Declare Variable to hold guess count
guess = 0
# Open loop
while userPassed == 0:
    # Ask user for input
    userInput = input("Enter a number between 1 and {}: ".format(intRange))
    # Error handling
    try:
        # Convert string to integer
        userInput = int(userInput)
        # Check if input equals answer
        if userInput == answer:
            # Increment by 1
            guess = guess + 1
            # Congratulate user
            print("You have guessed correctly it took you {} guesses to answer correctly".format(guess))
            # Increase value by 1, closes while loop
            userPassed = userPassed + 1
        # Check if input is greater than answer
        elif userInput > answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too high, you have guessed {} times so far".format(userInput, guess))
            # Call method to check guess
            CG = CheckGuess()
            CG.Call()
        # Check if input is less than answer
        elif userInput < answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too low, you have guessed {} times so far".format(userInput, guess))
            # Call method to check guess
            CG = CheckGuess()
            CG.Call()   
    except ValueError:
        # Increment by 1
        guess = guess + 1
        # Call method to check guess
        CG = CheckGuess()
        CG.Call()
        # Return message to user
        print("Please Enter a valid number")   

                    
