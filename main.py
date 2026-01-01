import sys
from stats import count, countChar, getSortedList

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # 1. check if the user provided a file path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2. grab the path from the arguments list
    book_path = sys.argv[1]
    
    # 3. use that path to get the text
    text = get_book_text(book_path) 

    # 4. process the data
    word_count = count(text)
    chars_dict = countChar(text)
    sorted_chars = getSortedList(chars_dict) 

    # 5. print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()