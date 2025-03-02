# commented out lines kept as a reminder of the steps took to build this first project
from stats import *
import sys

def get_book_text(path):
    try:
        with open(path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
        return ""
    except IOError:
        print(f"Error: An I/O error ocurred trying to read the file at '{path}'.")
        return ""
    
def main():
    if len(sys.argv) != 2:
        print("You also need to specify the path to the book, ex: python 3 main.py books/frankenstein.txt")
        sys.exit(1)
    bookpath = sys.argv[1]
    book_string = get_book_text(bookpath)
    num_words = words_count(book_string)
    #print(f"{num_words} words found in the document")
    characters = character_times(book_string)
    #print(characters)
    report = sorted_list(characters)
    #print(report)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_values in report:
        for char, count in sorted_values.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

main()