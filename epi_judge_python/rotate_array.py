import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount: int, A: List[int]) -> None:
    for i in range(len(A)//2):
        for j in range(len(A[0])//2):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    #reverse each row
    # for i,row in enumerate(A):
    #     A[i] = list(reversed(row))

    return A


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    print(rotate_array(90, [[1,2],[3,4]]))
    # exit(
    #     generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
    #                                    rotate_array_wrapper))
