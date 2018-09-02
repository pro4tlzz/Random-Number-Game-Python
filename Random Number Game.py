userPassed = 0
intRange = 30
answer = "5"
while userPassed == 0:
    userInput = input("Enter a number: ")
    if userInput == answer:
            print("You have guessed correctly")
            userPassed = userPassed + 1
    elif userInput > answer:
            print("Your answer was too high")
    elif userInput < answer:
            print("Your answer was too low")
    else:
            print("Enter a valid number")
                
    
    
