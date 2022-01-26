def list_sum(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum


numbers = [3, 4, 5, 6, 3, 33]

print(list_sum(numbers))
