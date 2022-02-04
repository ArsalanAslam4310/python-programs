def number_sum(list_of_numbers):
    sum = 0
    i =0
    while i < len(list_of_numbers):
        sum =sum + list_of_numbers[i]
        i = i +1
    return sum

list_of_numbers = [74,14,5,55,1]
add_list=number_sum(list_of_numbers)
print(add_list)
