def word_count(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry the file " + filename + " was not found."
        print(message)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['text_files/alice.txt','text_files/siddhartha.txt']
for filename in filenames:
    word_count(filename)
