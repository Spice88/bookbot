def count(file):

    num_words = 0

    with open(file) as f:
    
        file_contents = f.read()

        words = file_contents.split()

    for word in words:

        num_words += 1

    return num_words


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

    return num_chars


def sort_key(dictionary):
    
    return dictionary["num"]


def sort_this_book(file):

    first_dictionary = char_count(file)

    list_of_dictionaries = []

    for value in first_dictionary:
        
            second_dictionary = {}

            if value.isalpha():

                second_dictionary["letter"] = value

                second_dictionary["num"] = first_dictionary[value]

                list_of_dictionaries.append(second_dictionary)

    list_of_dictionaries.sort(reverse=True, key=sort_key)

    return list_of_dictionaries


