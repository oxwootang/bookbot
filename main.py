import sys
from stats import num_words, character_dictionary, sort_char_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    # returns the contents of the file as a string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

# def num_words(book_txt):
#     words = book_txt.split()
#     print(f"{len(words)} words found in the document")

def main():
    # print(get_book_text('books/frankenstein.txt'))
    # text = get_book_text('books/frankenstein.txt')
    # num_words(text)
    # print(character_dictionary(text))
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words(text)
    print("--------- Character Count --------")
    # print(sort_char_dict(character_dictionary(text)))
    list_chars = sort_char_dict(character_dictionary(text))
    for char in list_chars:
        print(f"{char["char"]}: {char["count"]}")

main()