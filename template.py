import sys

# Print debug messages
DEBUG = True


def debug(*args, **kwargs):
    if "file" not in kwargs.keys():
        kwargs |= {"file": sys.stderr}
    if DEBUG:
        print(*args, **kwargs)


def main():
    pass


if __name__ == '__main__':
    main()
