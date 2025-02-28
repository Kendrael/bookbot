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
    book_string = get_book_text("books/frankenstei.txt")
    print(book_string)

main()