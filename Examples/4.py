"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""
names = []

inital_id = id(names)
names.append('Tanu')
names.append('Aruna')
names.append('Kisa')
id_after_append = id(names)

if inital_id == id_after_append:
    print('Id has not been changed and is {inital_id}')
else:
    print('Id has been changed from {inital_id} to {id_after_append}')

names.sort()
print()
print('First item -> {names[0]}')
print('second item -> {names[1]}')
