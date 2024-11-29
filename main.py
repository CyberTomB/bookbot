def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text):
    return len(text.split())

def char_frequency(text):
    fdict = {}
    for char in text:
        lower_char = char.lower()
        if(lower_char not in fdict):
            fdict[lower_char] = 1
        else:
            fdict[lower_char] += 1
    return fdict

def main():
    print(char_frequency(read_file("./books/frankenstein.txt")))

main()