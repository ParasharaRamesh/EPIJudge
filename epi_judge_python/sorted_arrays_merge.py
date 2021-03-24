from typing import List
from copy import *
from test_framework import generic_test
from heapq import *

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    if len(sorted_arrays) == 0:
        return []
    if len(sorted_arrays) == 1:
        return sorted_arrays[0]
    minHeap = deepcopy(sorted_arrays[0])
    heapify(minHeap)
    for sorted_array in sorted_arrays[1:]:
        for ele in sorted_array:
            heappush(minHeap, ele)

    result = []
    for i in range(len(minHeap)):
        result.append(heappop(minHeap))
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sorted_arrays_merge.py','sorted_arrays_merge.tsv',merge_sorted_arrays))
