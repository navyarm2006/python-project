import random

number = random.randint(1,10)

while True :
    guess = int(input("Guess a number between 1 to 10 :"))

    if guess == number :
        print("Correct! You guessed the number . ")
        break
    elif guess > number :
        print("Too high, try again.")
    
    else:
        print("Too low, try again.")


