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
    
def words_count(book):
    words = len(book.split())
    return words

def main():
    book_string = get_book_text("books/frankenstein.txt")
    num_words = words_count(book_string)
    print(f"{num_words} words found in the document")

main()