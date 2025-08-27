from pathlib import Path
import sys
from stats import get_book_count
from stats import get_char_count
from stats import sort_count

def get_book_text(filepath): #function to return the file as a string
    with open(filepath, "r", encoding="utf-8") as file: #opens file in read only mode and sets it as f
        return file.read()                              #reads that file

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return
    filepath = Path(sys.argv[1])
    filepath_string = str(filepath) #This is just books/frankentein.txt not the actual book text
    word_count = get_book_count(filepath)
    sort_dict = sort_count(filepath) #count_list from stats.py
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {filepath_string}...\n")
    print(f"Found {word_count} total words\n")
    print(f"--------- Character Count -------\n")
    for item in sort_dict:
        print(f"{item['char']}: {item['num']}") #removing the char and num and prints each value pair once per line due to loop
main()
