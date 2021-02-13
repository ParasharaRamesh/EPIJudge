from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    r = list(reversed(A))
    for i in range(len(r)):
        if r[i] < 9:
            r[i]+=1
            break
        elif i == len(r) -1:
            r[i] = 0
            r.append(1)
        else:
            r[i] = 0
    return list(reversed(r))

if __name__ == '__main__':
    # print(plus_one([9]))
    # print(plus_one([9,9,9,9]))
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
