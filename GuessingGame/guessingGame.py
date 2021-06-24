import random

chances = 5
guess = 5




while chances > 0:
    chances = chances - 1
    print(chances)

    yourguess = int(input("Type in your guess"))

    randomNo = random.randint(1,9)
    
    if yourguess == randomNo:
        print("Congratulations you won!!!")
        break
    
    else:
        print ("You lose !!! the number is", randomNo)

    