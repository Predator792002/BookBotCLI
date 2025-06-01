from stats import word_count, char_count, report
import sys
def main(path):
    
    cnt = get_book_text(path)
    num_words = word_count(cnt)
    characters = char_count(cnt)
    sorted_dict = report(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}" )
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item["Char"]}: {item["num"]}")
    print("============= END ===============")

    


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def run():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])
run()
