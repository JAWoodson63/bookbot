import sys
from stats import num_of_words
from stats import num_of_characters
from stats import sorting

def get_book_text(path):
    with open(path, encoding='utf8') as f:
        contents = f.read()
    return contents

def main():
    # Retrieving book data
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(path)
    # Extracting book data
    num = num_of_words(book)
    chars = num_of_characters(book)
    # Sorting book data
    sorted = sorting(chars)

    # Printing book report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for key in sorted:
        print(f"{key["char"]}: {key["num"]}")
    print("============== End ==============")

main()