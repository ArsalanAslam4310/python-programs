# number guessing game
from random import randint

random_number = (randint(1, 50))
guess = 0
turns = 5

for turn in range(turns):
    guess = int(input("Enter a guess:"))
    if guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too big!")
    else:
        print("Correct number!")
    print(f"{turns-(turn+1)} turns remainig")
print("Game over")
