from typing import Iterator, List
from itertools import *
from test_framework import generic_test
from heapq import *

def sort_approximately_sorted_array(sequence: Iterator[int],k: int) -> List[int]:
    result = []
    heap = list(islice(sequence, k))
    heapify(heap)
    while True:
        try:
            result.append(heappop(heap))
            heappush(heap, next(sequence))
        except StopIteration:
            while heap:
                result.append(heappop(heap))
            break

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',sort_approximately_sorted_array_wrapper))
