import json

def add_favorite_number():
    """Add favorite number to file"""
    filepath = 'json_files/favorite_numbers.json'
    with open(filepath, 'w') as file_object:
        favorite = input("What is your favorite number? ")
        json.dump(favorite, file_object)
    return favorite

def read_favorite_number():
    """Read favorite number from file"""
    filepath = 'json_files/favorite_numbers.json'
    try:
        with open(filepath) as file_object:
            favorite = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favorite

def state_favorite_number():
    """Print out favorite number"""
    favorite = read_favorite_number()

    if favorite:
        print("I know your favorite number! It is " + favorite)
    else:
        favorite = add_favorite_number()
        print("I know your favorite number! It is " + favorite)

state_favorite_number()
