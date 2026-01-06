import sys
from stats import get_num_words, count_characters, get_sorted_character_counts


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    char_counts = count_characters(book_text)
    sorted_chars = get_sorted_character_counts(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()

