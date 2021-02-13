from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here
    count = 0
    finished = False
    while x > 0:
        if x & 1 == 1:
            count += 1
        x = x >> 1
    return count


if __name__ == '__main__':
    # count_bits(3)
    exit(generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',count_bits))
