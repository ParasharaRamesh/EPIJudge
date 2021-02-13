from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    specialIndex = len(perm) -1
    for i in range(len(perm)-1 , 0 , -1):
        if perm[i-1] >= perm[i]:
            specialIndex -=1
        else:
            break

    if specialIndex == 0:
        return []
    else:
        #find the next biggest ele after specialIndex -1
        prev = perm[specialIndex-1]
        specialIndexAfterPrev = len(perm) -1
        while specialIndexAfterPrev >= 0:
            if perm[specialIndexAfterPrev] > prev:
                break
            specialIndexAfterPrev-=1
        perm[specialIndexAfterPrev], perm[specialIndex-1] = perm[specialIndex-1], perm[specialIndexAfterPrev]
        return perm[:specialIndex] + list(reversed(perm[specialIndex:]))
    return []


if __name__ == '__main__':
    # print(next_permutation([1,3,4,2,0]))
    # print(next_permutation([1,3,2]))
    # print(next_permutation([3,2,1]))
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
