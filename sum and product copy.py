limit = int(input("Enter a limit:"))
choice = int(input("Enter 1 for sum or 2 for product:"))
sum = 0
product = 1

if choice == 1:
    for number in range(limit):
        sum = sum + number
    print(sum)
else:
    for number in range(limit):
        if number != 0:
            product = product * number
    print(product)
