"""
11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""
filename = '11_file_ext_name.cpp'


def get_name_and_extension(file):
    print('File Name: {file[:-4]}')
    print('Extension is: {file[-3: ]}')


get_name_and_extension(filename)
