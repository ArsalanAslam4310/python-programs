next_leap_year = 0
last_leap_year =2020
number_of_leap_years= 2

for year in range(number_of_leap_years):
    next_leap_year=last_leap_year+4
    last_leap_year= next_leap_year
    print(f"{year}.{next_leap_year}")
