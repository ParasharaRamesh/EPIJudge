from test_framework import generic_test
import math
from swap_bits import *

def set_ith_bit(n, i, value):
    return n  | (value << i)

def get_no_of_bits(x):
    if x&(x-1) != 0:
        no_of_bits = math.ceil(math.log(x, 2))
    else:
        no_of_bits = math.log(x,2) + 1
    return int(no_of_bits)

def reverse_bits_naive(x: int) -> int:
    i = get_no_of_bits(x) - 1
    reverse = 0
    while x:
        ithbit = x & 1
        reverse = set_ith_bit(reverse, i, ithbit)
        i -= 1
        x >>= 1
    return reverse

def reverse_bits(x: int) -> int:
    end = 63
    start = 0
    for i in range(32):
        x = swap_bits(x, start, end)
        start +=1
        end -= 1
    return x




if __name__ == '__main__':
    # print(reverse_bits(1351510410656)) # 405942121183313920
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
