'''14.Define a function which can read json file and displays the data present 
in it to the console in dictionary format
Note : Please create .json file and store the sample data in it and read the json file, 
display the data in dictionary format
'''

import json

def display_json(file1):
    with open(file1) as f:
        data = json.load(f)
        print(data)

print(display_json('file1.json'))
