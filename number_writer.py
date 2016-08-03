import json

numbers = [2,3,4,7,11,13]

filename = 'json_files/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
