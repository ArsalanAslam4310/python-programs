from math import sqrt

number = int(input("Enter a number:"))
flag = False

if number<=1==0:
    print(f"number{number} is not prime ")
else:
    for i in range(int(round(sqrt(number)))+1):
        if i>=2:
            if number%i ==0:
                flag = True
                break
if flag:
    print(f"The number{number} is not prime ")
else:
    print(f"THe number{number} is prime")

