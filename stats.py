def words_count(book):
    words = len(book.split())
    return words

def character_times(book_string):
    lowercase_string = book_string.lower()
    characters = {}
    for c in lowercase_string:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

def sorted_list(char_dict):
    count_chars = []
    for character in char_dict:
        count = char_dict[character]
        count_chars.append({character: count})
    def sort_on(dict_item):
        for value in dict_item:
            return dict_item[value]
    count_chars.sort(reverse=True, key=sort_on)
    return count_chars
