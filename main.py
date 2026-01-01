from stats import count, countChar

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    textPath = "books/frankenstein.txt"
    text = get_book_text(textPath) 
    num_words = count(text)
    print(f"Found {num_words} total words")

    dictionary = countChar(text)
    print(dictionary)
 
main()