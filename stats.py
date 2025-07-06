def count(file):

    num_words = 0

    with open(file) as f:
    
        file_contents = f.read()

        words = file_contents.split()

        for word in words:

            num_words += 1

    print(f"{num_words} words found in the document")

def char_count(file):
    
    num_chars = {}

    with open(file) as f:

        file_contents = f.read()

        file_contents_lower = file_contents.lower()

        words = file_contents_lower.split()

        for word in words:

            chars = list(word) 

            for char in chars:

                if char in num_chars:

                    num_chars[char] += 1

                else:

                    num_chars[char] = 1

    print(num_chars)
    