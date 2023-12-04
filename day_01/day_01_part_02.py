import sys

# Print debug messages
DEBUG = True

number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def debug(*args, **kwargs):
    if "file" not in kwargs.keys():
        kwargs |= {"file": sys.stderr}
    if DEBUG:
        print(*args, **kwargs)


def get_replaced(line):
    debug(f'Original line: {line}')
    for word, number in number_dict.items():
        line = line.replace(word, str(number))
    debug(f'Replaced line: {line}')
    return line


def get_number(line):
    # Replace spelled out numbers by real numbers
    line = get_replaced(line)
    # I need to find both first and last character on the line that is a number
    first = None
    last = None
    for letter in line:
        if '0' <= letter <= '9':
            if first is None:
                first = letter
            last = letter
    debug(f'first: {first}, last: {last}')
    return first + last


def main():
    number_list = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            debug(f'line: {line}')
            number = get_number(line)
            debug(f'number: {number}')
            number_list.append(number)
    result = sum(int(c) for c in number_list)
    print(f'Solution: {result}')


if __name__ == '__main__':
    main()
