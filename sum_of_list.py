def sum_of_list(list_of_numbers):
    sum =0
    
    for number in list_of_numbers:
        sum = sum +number
    return sum

list_of_numbers = [5,4,77,5,22,44]
sum_list = sum_of_list(list_of_numbers)
print(sum_list)