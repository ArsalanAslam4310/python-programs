def find_in_list(value, list_of_numbers):
    flag = True

    for number in list_of_numbers:
        if number == value:
            flag = False
            return flag

    if flag:
        return flag

numbers = [6, 5, 3, 66, 77, 9]
number_to_find = int(input("Enter a number:"))
number_found = find_in_list(number_to_find,numbers)

if number_found:
    print("not found")
else:
    print("found")    