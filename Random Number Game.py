import random
# Set Value for while loop
userPassed = 0
# Range of random
intRange = 100
# Declare random
answer = random.randint(1, 100)
# Open loop
while userPassed == 0:
    # Ask user for input
    userInput = input("Enter a number between 1 and 100: ")
    # Convert string to integer
    userInput = int(userInput)
    # Check if input equals answer
    if userInput == answer:
            # Congratulate user
            print("You have guessed correctly")
            # Increase value by 1, closes while loop
            userPassed = userPassed + 1
    # Check if input is greater than answer
    elif userInput > answer:
            # Return message to user
            print("Your answer was too high")
    # Check if input is less than answer
    elif userInput < answer:
            # Return message to user
            print("Your answer was too low")
    else:
            # Return message to user
            print("Enter a valid number")
                
    
    
