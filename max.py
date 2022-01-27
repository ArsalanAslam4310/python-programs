def maximum(list_of_numbers):
    max = 0
    for number in list_of_numbers:
        if max < number:
            max = number
    return max


def minimum(list_of_numbers):
    min = list_of_numbers[0]
    for number in list_of_numbers:
        if min > number:
            min = number
    return min


def bubble_sort(list_of_numbers):
    search_index = 0
    temp = 0
    min = 0
    for index in range(len(list_of_numbers)):
        min = minimum(list_of_numbers[index:])
        search_index = list_of_numbers.index(min)
        temp = list_of_numbers[index]
        list_of_numbers[index] = min
        list_of_numbers[search_index] = temp
    return list_of_numbers


numbers = [41, 24, 11, 50, 89, 32, 60, 49, 34,
           87, 37, 74, 39, 63, 76, 45, 59, 97, 66]

sorted = bubble_sort(numbers)
print(sorted)
