from stats import word_count, get_chars_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    chars_dict = get_chars_dict(text)

    print(f"Found {word_count(text)} total words")
    print(chars_dict)

main()
