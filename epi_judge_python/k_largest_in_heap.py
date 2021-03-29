from collections import deque
from typing import List
from math import *
from heapq import *
from test_framework import generic_test, test_utils


def insert_into_limited_min_heap(x, minheap, limit):
    if len(minheap) < limit:
        heappush(minheap, x)
    elif x >= minheap[0]:
        heappop(minheap)
        heappush(minheap, x)


def getNeighbours(A, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    n = len(A) - 1
    #here is the issue bro
    leftExceeded = l > n
    rightExceeded = r > n

    if leftExceeded and rightExceeded:
        return []
    elif rightExceeded:
        return [(A[l],l)]
    else:
        return [(A[l], l), (A[r], r)]


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    if k == len(A):
        return A
    klarge = []
    q = deque([(A[0], 0)])
    while q:
        x, ind = q.popleft()
        insert_into_limited_min_heap(x, klarge, k)
        neighbours = getNeighbours(A, ind)
        q.extend(neighbours)
    return sorted(klarge, reverse= True)


if __name__ == '__main__':
    # print(k_largest_in_binary_heap([561, 314, 401, 28, 156, 359, 271, 11, 3], 2))
    # print(k_largest_in_binary_heap([561, 314, 401, 28, 156, 359, 271, 11, 3], 4))
    # print(k_largest_in_binary_heap([10, 2, 9, 2, 2, 8, 8, 2, 2, 2, 2, 7, 7, 7, 7], 5))
    # print(k_largest_in_binary_heap([10, 9, 8, 2, 2, 6, 7], 5))
    #[21, 20, 20, 19, 18, 18, 18, 16, 16, 16, 14, 14, 11, 9, 9]
    # print(k_largest_in_binary_heap([21, 20, 18, 16, 20, 16, 14, 11, 16, 19, 18, 9, 5, 2, 9, 8, 3, 1, 0, 14, 3, 18], 15))
    exit(generic_test.generic_test_main('k_largest_in_heap.py', 'k_largest_in_heap.tsv', k_largest_in_binary_heap,comparator=test_utils.unordered_compare))
