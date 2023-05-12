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


def hash_function(pattern: str):
    # create a hash function
    hpattern = 0
    for i in range(len(pattern)):
        hpattern += ord(pattern[i]) * 263 ** i

    return hpattern


def get_occurrences(pattern: str, text: str):
    # create an empty list to store the occurencies
    occurencies = []
    # create a hash function
    hpattern = hash_function(pattern)

    # iterate over the text and check if the hash of the pattern is equal to the hash of the text
    for i in range(len(text) - len(pattern) + 1):
        if hash_function(text[i:i + len(pattern)]) == hpattern:
            occurencies.append(str(i))

    return occurencies


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

