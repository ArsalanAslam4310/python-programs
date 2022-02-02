import numbers


numbers = int(input("Enter a number!"))
sum =0

for number in range(17):
    if numbers%3==0 or numbers%5==0:
        sum = sum + numbers
print(sum)