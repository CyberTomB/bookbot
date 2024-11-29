def read_file(path):
    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(contents):
    return len(contents.split())


def main():
    print(count_words(read_file("./books/frankenstein.txt")))

main()