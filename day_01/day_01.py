import sys

# Print debug messages
DEBUG = True


def debug(*args, **kwargs):
    if "file" not in kwargs.keys():
        kwargs |= {"file": sys.stderr}
    if DEBUG:
        print(*args, **kwargs)


def get_number(line):
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
