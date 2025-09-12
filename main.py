import sys
from stats import get_num_words, get_num_characters, sortvert

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    total = get_num_words(sys.argv[1])
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    counts = get_num_characters(sys.argv[1])
    sorted_list = sortvert(counts)
    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()