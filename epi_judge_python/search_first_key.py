from typing import List
from bisect import *
from test_framework import generic_test


def binarySearchLeft(A, k):
    l = 0
    r = len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] < k:
            l = m + 1
        else:
            r = m

    return l


# to the right of the element
def binarySearchRight(A, k):
    l = 0
    r = len(A) - 1
    ind = None
    while l < r:
        m = (l + r) // 2
        if A[m] <= k:
            l = m + 1
        else:
            r = m
    if l == len(A) - 1 and A[l] == k:
        return l + 1
    elif A[l-1] == k:
        return l
    else:
        return -1


def search_first_of_k(A: List[int], k: int) -> int:
    i = binarySearchLeft(A, k)
    if i <= len(A) - 1 and A[i] == k:
        return i
    return -1


def search_first_of_k_using_bisect(A: List[int], k: int) -> int:
    i = bisect_left(A, k)
    if i <= len(A) - 1 and A[i] == k:
        return i
    return -1

if __name__ == '__main__':
    # print(binarySearchLeft([0,1,2,3],0))
    # print(binarySearchLeft([0,1,2,3],1))
    # print(binarySearchLeft([0,1,2,3],2))
    # print(binarySearchLeft([0,1,2,3],3))
    # print(binarySearchLeft([0,1,2,3],4))
    # print(binarySearchLeft([0,1,2,3],-2))
    exit(generic_test.generic_test_main('search_first_key.py','search_first_key.tsv',search_first_of_k))
