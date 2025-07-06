def get_book_text(file):

    file_contents = file.read()

    return file_contents

def main():
    
    with open("books/frankenstein.txt") as f:

        print(get_book_text(f))

from stats import count

from stats import char_count

count("books/frankenstein.txt")

char_count("books/frankenstein.txt")