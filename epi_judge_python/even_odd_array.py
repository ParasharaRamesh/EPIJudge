import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(a: List[int]) -> None:
    # TODO - you fill in here.
    e = 0
    o = len(a)-1
    while e < o:
        if a[e] % 2 == 0:
            e+=1
        else:
            a[e], a[o] = a[o], a[e]
            o-=1
    return a


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    # print(even_odd([1,2,3,4,5,6, 7 , 8]))
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
