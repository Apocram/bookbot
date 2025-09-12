from stats import get_num_words, get_num_characters, sortvert

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    total = get_num_words("books/frankenstein.txt")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    counts = get_num_characters("books/frankenstein.txt")
    sorted_list = sortvert(counts)
    for d in sorted_list:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()