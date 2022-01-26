previous_number = 1
current_number = 1
next_number = previous_number + current_number
sum = 0

while next_number <= 4000000:
    previous_number = current_number
    current_number = next_number
    next_number = previous_number + current_number
    if next_number % 2 == 0:
        sum += next_number

print(sum)
