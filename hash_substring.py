def read_input():
    method: str = input()[0]
    match method:
        # read from input
        case "I":
            pattern: str = input().rstrip()
            text: str = input().rstrip()
        # read from file
        case "F":
            with open("tests/06", 'r') as file:
                content: list = file.readlines()
                pattern: str = content[0].rstrip()
                text: str = content[1].rstrip()

    return (pattern, text)
    

def print_occurrences(output: list):
    print(' '.join(map(str, output)))


def hash_function(text: str, i: int, chash: int = 0, len_pattern: int = 0) -> int:
    # create a hash function
    cur_hash = chash
    if i > 0 and i <= len(text) - len_pattern + 1:
        cur_hash -= ord(text[i - 1]) * 263 
        cur_hash += ord(text[i + len_pattern - 1]) * 263 
    elif (i == 0):
        cur_hash = 0
        for j in range(i + len_pattern):
            cur_hash += ord(text[j]) * 263 
    elif (i == -1):
        len_pattern = len(text)
        cur_hash = 0
        for j in range(len_pattern):
            cur_hash += ord(text[j]) * 263 
    return cur_hash


def get_occurrences(pattern: str, text: str):
    # create an empty list to store the occurences
    occurrences = []
    hpattern = hash_function(pattern, -1)
    len_pattern = len(pattern)

    # iterate over the text and check if the hash of the pattern is equal to the hash of the text
    cur_hash = 0
    for i in range(len(text) - len(pattern) + 1):
        tpattern = hash_function(text, i, cur_hash, len_pattern)
        cur_hash = tpattern
        if cur_hash == hpattern:
        # if the hash values match, check character by character if the pattern matches the text
            occurrences.append(str(i))

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

