def occur_in_list(list_of_numbers):
    number = int(input("Enter a number:"))
    if number in list_of_numbers:
        print("yes")
    else:
        print("Not")
    return number

list_of_numbers = [55,44,8,7,2,1]
occur= occur_in_list(list_of_numbers)
print(occur)