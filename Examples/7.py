"""
7. Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""
from functools import  reduce

people_data = ([('Reenika', 'Bhatta', 21), ('Bishal', 'Khanal', 22),
               ('Prakash', 'Aryal', None), ('Jaya', 'Kc', 23)])

ages = [x[2] for x in people_data]
sum_of_ages = 0
age_count = 0
for age in ages:
    if age is not None:
        age_count += 1
        sum_of_ages += age

avg_age = sum_of_ages / age_count


for first_name, last_name, age in people_data:
    print('{first_name} {last_name}', end=' ')
    if age is not None:
        if age < avg_age:
            print('young')
        else:
            print('old')
    else:
        print('Unknown')
