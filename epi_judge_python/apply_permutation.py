from typing import List

from test_framework import generic_test
import copy

#with extra space
# def apply_permutation(perm: List[int], A: List[int]) -> None:
#     permuted = [None] * len(perm)
#     for i, x in enumerate(zip(perm, A)):
#         p , a = x
#         permuted[p] = a
#     A.clear()
#     A.extend(permuted)
#     return permuted

def apply_permutation(perm, A) -> None:
    i = 0
    while i < len(perm):
        actualPos = perm[i]
        if i != actualPos:
            A[i], A[actualPos]  = A[actualPos], A[i]
            perm[i], perm[actualPos]  = perm[actualPos], perm[i]
        else:
            i+=1
    # return A, perm

def apply_inverse(perm, A):
    augmentedA = [(a, i) for i,a in enumerate(A)]
    apply_permutation(perm , augmentedA)
    inverse_perm = [x[1] for x in augmentedA]
    apply_permutation(inverse_perm, A)
    return A

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    # print(apply_permutation([2,0,1,3],['a','b','c','d']))
    # print(apply_inverse([1,0,3,4,2],['a','b','c','d','e']))
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
