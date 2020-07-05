"""
2. Write an if statement to determine whether a variable holding a year
is a leap year.
"""

year = 1904

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{year} is a leap year.')
        else:
            print('{year} is not a leap year.')
    else:
        print('{year} is a leap year.')
