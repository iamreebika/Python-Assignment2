"""
13. Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
"""
import csv
details_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]


def write_csv(sample_list):
    with open('personal_file.csv', 'w', newline='') as personal_details:
        detail_writer = csv.writer(personal_details)
        header_row = ['name', 'address', 'age']
        detail_writer.writerow(header_row)
        for detail in sample_list:
            detail_writer.writerow(list(detail))
    personal_details.close()


write_csv(details_list)
