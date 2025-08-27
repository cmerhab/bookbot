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
                char_count[char] += 1 #found second time or more
            else:
                char_count[char] = 1 #found first time
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"An error occured: {e}")
    return char_count

def sort_on(item):
    return item["num"] #returns the value in the num
 
def sort_count(filepath):
    dict = get_char_count(filepath)

    count_list = [{"char": char, "num": count} for char, count in dict.items() ] #.items() makes the list into key value pairs
    count_list.sort(reverse=True, key=sort_on) #runs the sort_on function as the key
    return count_list