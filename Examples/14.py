"""
14. Write a function that reads a CSV file. It should return a list of
dictionaries, using the first row as key names, and each subsequent
row as values for those keys.
For the data in the previous example it would return:
[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
'John', 'address': '54 Love Ave', 'age': 21}]
"""
import csv


def read_data(file_name):
    result_data_list = []
    with open(file_name, newline='') as file:
        file_reader = csv.reader(file, delimiter=',')
        is_first_row = True
        for data in file_reader:
            temp_dict = {}
            if is_first_row:
                keys = data
                is_first_row = False
                continue
            for i in range(len(keys)):
                temp_dict[keys[i]] = data[i]
            result_data_list.append(temp_dict)
    file.close()
    return result_data_list


print(read_data('personal_file.csv'))
