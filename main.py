import sys

if len(sys.argv) != 2:

    print("Usage: python3 main.py <path_to_book>")

    sys.exit(1)


def get_book_text(file):

    file_contents = file.read()

    return file_contents


def main():
    
    with open(sys.argv[1]) as f:

        print(get_book_text(f))


from stats import count

from stats import char_count

from stats import sort_this_book

from stats import sort_key


def main_2(file):

        print("=========== BOOKBOT ===========")
        print(f"Analyzing book found at {file}...")
        print("---------- Word Count ---------")
        print(f"Found {count(file)} total words")
        print("-------- Character Count ------")

        list_1 = []
        list_1 = sort_this_book(file)

        for line in list_1:

            print(f"{line["letter"]}: {line["num"]}")

        print("============= END =============")


main_2(sys.argv[1])
