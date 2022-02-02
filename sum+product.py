limit = int(input("Enter a limit:"))
choice = int(input("Enter 1 for product and 2 for sum:"))
sum = 0
product =1

if choice ==1:
    for number in range(limit):
        if number !=0:
            product = product*number
    print(product)
else:
    for number in range(limit):
        sum = sum + number
    print(sum)