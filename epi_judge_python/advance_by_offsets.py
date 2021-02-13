from typing import List
from functools import lru_cache
from collections import defaultdict
from test_framework import generic_test

def memoise(func):
    cache = {}
    def wrapper(A):
        key = tuple(A)
        if key not in cache:
            cache[key] = func(A)
        return cache[key]

    return wrapper


@memoise
def can_reach_end_top_down(A: List[int]) -> bool:
    # TODO - you fill in here.
    if len(A) == 0:
        return False
    if len(A) == 1:
        return True
    if len(A) == 2:
        return A[0] > 0

    x = A[0]

    canReach = False

    for j in range(1, x+1):
        canReach = canReach or can_reach_end(A[j:])

    return canReach

def can_reach_end(A: List[int]) -> bool:
    i = 0
    furthest_reach = 0
    while i < len(A)-1:
        furthest_reach = max(furthest_reach, A[i] + i if A[i] > 0 else A[i])
        i+=1
    return furthest_reach >= len(A) -1

#bottom up solution taking too much time!
# def can_reach_end(A: List[int]) -> bool:
#     bottomUpCache = defaultdict(lambda: False)
#
#     length = len(A)
#     bottomUpCache[length -1] = True
#
#     for i in range(length-2, -1, -1):
#         x = A[i]
#         if x >= length -1 - i:
#             bottomUpCache[i] = True
#         else:
#             bottomUpCache[i] = False
#             for j in range(1, x+1):
#                 if i + j < length and bottomUpCache[i+j]:
#                     bottomUpCache[i] = True
#                     break
#     return bottomUpCache[0]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
