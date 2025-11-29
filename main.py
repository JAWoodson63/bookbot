from stats import num_of_words
from stats import num_of_characters

def get_book_text(path):
    with open(path, encoding='utf8') as f:
        contents = f.read()
    return contents

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    num = num_of_words(book)
    chars = num_of_characters(book)

    print(f"Found {num} total words")
    for key in chars:
        print(f"'{key}': {chars[key]}")

main()