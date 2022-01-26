def max_number(list):
    max = 0
    for number in list:
        if max < number:
            max = number
    return max


list_of_numbers1 = [1, 5, 77, 99, 4, 6]
list_of_numbers2 = [2, 4, 46, 66, 77, 456, 33]
x = max_number(list_of_numbers1)
y = max_number(list_of_numbers2)
print(x, y)
