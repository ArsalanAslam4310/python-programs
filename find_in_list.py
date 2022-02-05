def find_in_list(value,list_of_numbers):
    flag = True

    for number in list_of_numbers:
        if number == value:
            flag +False
            return flag
    if flag:
        return flag

numbers = [55,11,44,2,3,5]
number_to_find= int(input("Enter a number:"))
found=find_in_list(number_to_find,numbers)

if found:
    print("Not found")
else:
    print("found")
        
        