from pathlib import Path
from stats import get_book_count
from stats import get_char_count
from stats import sort_count

def get_book_text(filepath): #function to return the file as a string
    with open(filepath, "r", encoding="utf-8") as file: #opens file in read only mode and sets it as f
        return file.read()                              #reads that file

def main():
    filepath = Path("books/frankenstein.txt")
    #print(get_book_text(filepath))
    filepath_string = str(filepath) #This is just books/frankentein.txt not the actual book text
    word_count = get_book_count(filepath)
    sort_dict = sort_count(filepath)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath_string}...\n")
    print(f"Found {word_count} total words\n")
    print(f"--------- Character Count -------\n")
    print(f"{sort_dict}")
main()
