import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook


def rearrange(A: List[int]) -> None:
    # TODO - you fill in here.
    i = 0
    nextShouldBeGreater = True

    while i < len(A) - 1:
        if nextShouldBeGreater:
            if A[i] > A[i + 1]:
                if i == 0:
                    A[i], A[i+1] = A[i+1] ,A[i]
                elif A[i-1] >= max(A[i],A[i+1]):
                    A[i], A[i+1] = A[i+1] ,A[i]
                else:
                    # find next biggest  from i+1 and swap with A[i+1]
                    nextBiggestIndex = i+1
                    j = nextBiggestIndex

                    while j < len(A):
                        if A[j] >= A[i]:
                            nextBiggestIndex = j
                            break
                        j+=1
                    A[nextBiggestIndex], A[i+1] = A[i+1] , A[nextBiggestIndex]
        else:
            if A[i] < A[i + 1]:
                if i == 0:
                    A[i], A[i+1] = A[i+1] ,A[i]
                elif A[i-1] <= min(A[i],A[i+1]):
                    A[i], A[i+1] = A[i+1] ,A[i]
                else:
                    # find next smalled and swap with A[i+1]
                    nextSmallestIndex = i + 1
                    j = nextSmallestIndex

                    while j < len(A):
                        if A[j] <= A[i]:
                            nextSmallestIndex = j
                            break
                        j += 1
                    A[nextSmallestIndex], A[i+1] = A[i+1], A[nextSmallestIndex]

        nextShouldBeGreater ^= True
        i += 1

    return A


@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                        i, 'A[{}] <= A[{}]'.format(i - 1, i),
                        '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] >= A[{}]'.format(i, i + 1),
                            '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] >= A[{}]'.format(i - 1, i),
                            '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i, i + 1),
                            '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    # print(rearrange([53, 32, 63, 44, 68, 26, 54, 49, 48, 59, 63, 32, 46, 37, 7, 61, 38, 57, 47, 71, 17, 50, 54, 14, 41, 28, 63, 67, 18, 34, 44, 65, 62, 40, 61, 38, 13, 4, 16, 36, 8, 50, 29, 11, 30, 64, 54, 45, 70, 70, 61, 61, 58, 52, 71, 75, 48, 74, 57, 6, 19, 14, 24, 28, 68, 8, 47, 1, 39, 20, 26, 58, 61, 45, 70, 9, 48, 34]))
    # print(rearrange([3,2,1,0]))
    exit(
        generic_test.generic_test_main('alternating_array.py',
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
