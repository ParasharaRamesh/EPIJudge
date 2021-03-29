from typing import List
from bisect import *
from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    i = bisect_left(A, k)
    if i <= len(A)-1 and A[i] == k:
        return i
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
