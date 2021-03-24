from typing import Iterator, List
from heapq import *
from test_framework import generic_test
from itertools import *

def online_median(sequence: Iterator[int]) -> List[float]:
    maxHeap = []
    minHeap = []
    medians = []
    isEvenIndex = True
    for x in sequence:
        if isEvenIndex:
            if len(maxHeap) == 0:
                heappush(maxHeap, -x)
            elif x <= minHeap[0]:
                heappush(maxHeap, -x)
            else:
                mp = heappop(minHeap)
                heappush(maxHeap, -mp)
                heappush(minHeap, x)
            medians.append(float(-maxHeap[0]))
        else:
            if len(minHeap) == 0:
                if x >= -maxHeap[0]:
                    heappush(minHeap, x)
                else:
                    mp = heappop(maxHeap) * -1
                    heappush(minHeap, mp)
                    heappush(maxHeap, -x)
            elif x >= -maxHeap[0]:
                heappush(minHeap, x)
            else:
                mp = heappop(maxHeap) * -1
                heappush(minHeap, mp)
                heappush(maxHeap, -x)
            medians.append((minHeap[0] - maxHeap[0])/2)
        isEvenIndex ^= True
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    # print(online_median_wrapper([1, 0, 3, 5, 2, 0, 1]))
    # print(online_median_wrapper([1, 2,3,4,5,6]))
    # print(online_median_wrapper([4,3,2,1,0]))
    exit(generic_test.generic_test_main('online_median.py', 'online_median.tsv', online_median_wrapper))
