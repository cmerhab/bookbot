from pathlib import Path

def get_book_count(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            words = content.split() #splits the string into a list of individual words
            count = len(words)
            return count
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found!")
        return 0
    

def get_char_count(filepath):
    char_count = {} #empty dictionary 
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            text = content.lower() # converts it all to lowercase

        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occured: {e}")
    return char_count