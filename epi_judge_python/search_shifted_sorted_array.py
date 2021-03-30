from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    smallest = None
    n = len(A) - 1
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if A[m] < A[-1]:
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    exit(generic_test.generic_test_main('search_shifted_sorted_array.py', 'search_shifted_sorted_array.tsv',search_smallest))
