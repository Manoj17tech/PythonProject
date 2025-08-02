# 1. Generate a random b/w 1-20
# 2. user has to guess the Number
# 3. guess == random Number (Correct Guess)
# 4. guess > rn  (too High)
# 5. guess < rn (too low)

# random : it generate the Random number , in the Given Interval of Numbers

# import : to import / use the Specified in our Code.

import random

randomNumber = random.randint(1,20)

# print(randomNumber)

while True:
    userGuess = int(input("Enter a Guess: "))

    if(userGuess == randomNumber):
        print("Correct Guess 🎉🥳")
        break

    elif(userGuess > randomNumber):
        print("Too High 📈")

    else: print("Too Low 📉")



# ROCK-PAPER-SCISSOR

# you have to choose between RPS [list] (Manually)

# Comnputer [list] => random Choose 


# import random 

# Winning Criteria : 10 (winner)

# choices = ['rock','paper','scissor']

# # randomChoice = random.choice(choices) # computer
# # print(randomChoice)

# userChoice = input(f"Enter the Choice: ").lower()

# computerChoice = random.choice(choices)

# # print(f"User Choice {userChoice}")
# print(f'Computer Choice {computerChoice}')

# if(userChoice == computerChoice):
#     print("It's a TIE")

# elif(userChoice=='rock' and computerChoice=='scissor' \
#     or userChoice=='paper' and computerChoice=='rock' \
#     or userChoice == 'scissor' and computerChoice == 'paper'):

#     print("You Won 😎")

# else: print("Computer Wins")



