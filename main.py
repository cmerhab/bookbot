from pathlib import Path
def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f: #opens file in read only mode and sets it as f
        return f.read()                              #reads that f file

def main():
    filepath = Path("books/frankenstein.txt")
    print(get_book_text(filepath))

main()
