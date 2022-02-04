def max_number(list_of_numbers):
    max = 0
    for i in list_of_numbers:
        if max < i:
            max = i 

    return max

list_of_numbers =[4,55,8,7,44,22,44]
maximium =max_number(list_of_numbers)
print(maximium)