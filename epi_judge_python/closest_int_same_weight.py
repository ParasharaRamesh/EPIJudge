from test_framework import generic_test
import math
from swap_bits import *

def getNoOfBits(x):
    if x > 0:
        if x&(x-1) != 0:
            return math.ceil(math.log(x, 2))
        else:
            return int(math.log(x,2) + 1)
    return 1

def getOnesComplement(x):
    return 2**getNoOfBits(x) - 1 - x

#get the least set 1 and get the log of that to get the index
def getIndexOfLeastSetOne(x, size):
    if x > 0:
        return int(math.log2(x & ~(x - 1)))
    return size

def getIndexOfLeastZero(x, size):
    complement = getOnesComplement(x)
    return getIndexOfLeastSetOne(complement, size)

def closest_int_same_bit_count(x: int) -> int:
    lsb = x&1
    size = getNoOfBits(x)
    indexOfLeastSetOne = getIndexOfLeastSetOne(x, size)
    indexOfLeastSetZero = getIndexOfLeastZero(x, size)

    bitsToFlip = (indexOfLeastSetOne, indexOfLeastSetOne - 1)
    if lsb:
        bitsToFlip = (indexOfLeastSetZero,indexOfLeastSetZero-1)

    mask = (1 << bitsToFlip[0]) | (1 << bitsToFlip[1])
    return x^mask


if __name__ == '__main__':
    # print(closest_int_same_bit_count(3))
    # print(closest_int_same_bit_count(48)) # 0b110000, and the expected in binary is 0b101000
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
