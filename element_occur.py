def occur_in_list(list_of_numbers,number):
    if number in list_of_numbers:
        print("yes")
    else:
        print("Not")

list_of_numbers = [55,44,8,7,2,1]
number = int(input("Enter a number:"))
occur_in_list(list_of_numbers,number)
