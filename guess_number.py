import random
random_number =random.randint(1,50)
guess = 0
turns = 5

for turn in range(turns):
    guess =int(input("Enter a guess:"))
    if guess>random_number:
        print("Too big")
    elif guess<random_number:
        print("Too small")
    else:
        print("Correct number")
    print(f"{turns - (turn+1)}.remaining Guess")
print("game over")