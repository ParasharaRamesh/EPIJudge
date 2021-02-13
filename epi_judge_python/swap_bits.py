from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    ithbit = (x >> i) & 1
    jthbit = (x >> j) & 1
    mask = (1 << i) | (1 << j) 
    if i == j or not (ithbit ^ jthbit):
        #no swap neccessary
        return x
    else:
        return x ^ mask


if __name__ == '__main__':
    # print(swap_bits(6,0,1))
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
