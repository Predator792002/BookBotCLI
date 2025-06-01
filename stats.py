def word_count(book_string):
    words = book_string.split()
    return len(words)

def char_count(book_string):
    lower_words = book_string.lower()
    char_dict = {}
    for char in lower_words:
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def report(dir):
    list_directory = []
    for key in dir:
        list_directory += [{"Char":key , "num":dir[key]}]
    list_directory.sort(reverse=True, key=sort_on)

    return list_directory
