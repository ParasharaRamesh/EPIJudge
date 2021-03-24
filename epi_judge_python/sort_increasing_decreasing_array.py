from typing import List
from heapq import *
from test_framework import generic_test
from collections import deque

def find_each_sequence(a):
    increasing = True
    sequences = [deque([a[0]])]
    for i in range(1,len(a)):
        if increasing and a[i-1] <= a[i]:
            sequences[-1].append(a[i])
        elif not increasing and a[i-1] >= a[i]:
            sequences[-1].appendleft(a[i])
        else:
            increasing ^= True
            sequences.append(deque([a[i]]))
    return list(map(lambda x: list(x), sequences))



def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sequences = find_each_sequence(A)
    return list(merge(*sequences))


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sort_increasing_decreasing_array.py','sort_increasing_decreasing_array.tsv',sort_k_increasing_decreasing_array))
