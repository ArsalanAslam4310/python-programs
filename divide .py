from math import sqrt

number = int(input("Enter a number"))
flag = False
if number%3== 0 and number%5 == 0:
    print(f"number{number} is divible by 3 and 5")
elif number <= 1:
    print(f"number{number} is not divisible by 3 and 5")
else:
    for i in range(int(round(sqrt(number)))+1):
        if i>=2:
            if number %i==0:
                flag = True
                break
    if flag:
        print(f"The number{number}is not prime")
    else:
        print(f"The number{number}is prime")      

