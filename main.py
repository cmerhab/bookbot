from pathlib import Path
def get_book_text(filepath): #function to return the file as a string
    with open(filepath, "r", encoding="utf-8") as file: #opens file in read only mode and sets it as f
        return file.read()                              #reads that file

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
def main():
    filepath = Path("books/frankenstein.txt")
    #print(get_book_text(filepath))
    word_count = get_book_count(filepath)
    print(f"{word_count} words found in the document")

main()
