first_number = input("\nFirst number: ")
try:
    first_number = int(first_number)
except ValueError:
    print("Please enter numbers instead of text.")

second_number = input("\nSecond number: ")
try:
    second_number = int(second_number)
except ValueError:
    print("Please enter numbers instead of text.")
else:
    print(first_number + second_number)
