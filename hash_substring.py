def read_input():
    method: str = input()[0]
    match method:
        case "I":
            pattern: str = input()
            text: str = input()
        case "F":
            with open("tests/06", 'r') as file:
                content: list = file.readlines()
                pattern: str = content[0].rstrip()
                text: str = content[1].rstrip()

    return (pattern, text)
    

def print_occurrences(output: list):
    print(' '.join(map(str, output)))


def get_occurrences(pattern: str, text: str):
    occurencies = []
    hpattern = hash(pattern)

    for i in range(len(text) - len(pattern) + 1):
        if hash(text[i:i + len(pattern)]) == hpattern:
            occurencies.append(str(i))

    return occurencies


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

