from test_framework import generic_test


def add(a, b):
    return a if b == 0 else add(a ^ b, (a & b) << 1)


def multiply(x: int, y: int) -> int:
    # adding x , y times
    mul = 0
    while y:
        if y & 1:
            mul = add(mul, x)
        y = y >> 1
        x = x << 1
    return mul


if __name__ == '__main__':
    # print(add(41,27))
    # print(multiply(3, 3))
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
