def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_year_leap(int(input("Input the year: "))))