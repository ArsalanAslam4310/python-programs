def sum_odd_numbers(list_of_numbers):
    sum =0
    
    for number in list_of_numbers:
        if number%2 != 0:
            sum = sum + number

    return sum

list_of_numbers = [3,41,56,47,58,1]
odd_numbers=sum_odd_numbers(list_of_numbers)
print(odd_numbers)