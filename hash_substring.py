def read_input():
    method: str = input("Input method I - manual input, F - files: ")[0]
    match method:
        case "I":
            pattern: str = input("Input pattern: ")
            text: str = input("Input text: ")
        case "F":
            filename: str = input("Input filename: ")
            file_path: str = "tests/"
            with open(file_path + filename, 'r') as file:
                content: list = file.readlines()
                pattern: str = content[0].strip()
                text: str = content[1].strip()

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

