def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text):
    return len(text.split())

def letter_frequency(text):
    fdict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for char in text:
        lower_char = char.lower()
        try:
            fdict[lower_char] += 1
        except:
            continue

    return fdict

def convert_dict_to_list(dict):
    arr = []
    for key, value in dict.items():
        arr.append({
            "name": key,
            "count": value
        })
    return arr

def sort_by_count(dict):
    return dict["count"]

def main(file_location = "./books/frankenstein.txt"):
    document = read_file(file_location)
    word_count = count_words(document)
    frequencies = convert_dict_to_list(letter_frequency(document))
    print(f"--- Begin report of ${file_location} ---")

    print(f"{word_count} words found in the document \n")
    for w in sorted(frequencies, key=sort_by_count, reverse=True):
        print(f"The {w['name']} character was found {w['count']} times")

    print("--- End report ---")

main()