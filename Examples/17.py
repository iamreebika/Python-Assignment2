"""
18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
"""

import json

personal_details = {
    'name': 'Reebika',
    'age': 22,
    'hobbies': ['travelling', 'Learningnewthings']
}
json_info = json.dumps(personal_details, indent=4)
print(json_info)  # json string

python_form = json.loads(json_info)
print(python_form)  # python form
