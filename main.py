from pathlib import Path
from stats import get_book_count
from stats import get_char_count

def get_book_text(filepath): #function to return the file as a string
    with open(filepath, "r", encoding="utf-8") as file: #opens file in read only mode and sets it as f
        return file.read()                              #reads that file

def main():
    filepath = Path("books/frankenstein.txt")
    #print(get_book_text(filepath))
    word_count = get_book_count(filepath)
    print(f"{word_count} words found in the document")
    char_count = get_char_count(filepath)
    print(f"{char_count}")
main()
