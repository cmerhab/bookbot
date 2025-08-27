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