from test_framework import generic_test


def snake_string(s: str) -> str:
    top = []
    middle = []
    bottom = []

    for i, ch in enumerate(s[1 : len(s): 4]):
        top.append(ch)

    for i,ch in enumerate(s[0 : len(s): 2]):
        middle.append(ch)

    for i,ch in enumerate(s[3 : len(s): 4]):
        bottom.append(ch)

    return ''.join(top + middle + bottom)


if __name__ == '__main__':
    # print(snake_string("Hello World!"))
    exit(generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',snake_string))
