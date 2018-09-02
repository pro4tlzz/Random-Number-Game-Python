import random
# Set Value for while loop
userPassed = 0
# Range of random
intRange = 100
# Declare random
answer = random.randint(1, 100)
# Declare Variable to hold guess count
guess = 0
# Open loop
while userPassed == 0:
    # Ask user for input
    userInput = input("Enter a number between 1 and 100: ")
    # Error handling
    try:
        # Convert string to integer
        userInput = int(userInput)
        # Check if input equals answer
        if userInput == answer:
            # Increment by 1
            guess = guess + 1
            # Congratulate user
            print("You have guessed correctly")
            # Increase value by 1, closes while loop
            userPassed = userPassed + 1
        # Check if input is greater than answer
        elif userInput > answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too high, you have guessed {} times so far".format(userInput, guess))
        # Check if input is less than answer
        elif userInput < answer:
            # Increment by 1
            guess = guess + 1
            # Return message to user
            print("Your answer {} was too low, you have guessed {} times so far".format(userInput, guess))
    except ValueError:
        # Increment by 1
        guess = guess + 1
        # Return message to user
        print("Please Enter a valid number")   
