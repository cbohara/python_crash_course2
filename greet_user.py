import json

filename = 'json_files/username.json'

with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back, " + username + "!")
