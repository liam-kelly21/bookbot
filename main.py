from stats import *
import sys

def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    words = get_words(text)
    freqs = sort_freqs(get_freq(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in freqs:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()