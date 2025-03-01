from stats import *

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
    bookpath = "books/frankenstein.txt"
    book_string = get_book_text(bookpath)
    num_words = words_count(book_string)
    print(f"{num_words} words found in the document")
    characters = character_times(book_string)
    print(characters)
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