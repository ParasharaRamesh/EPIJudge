from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque
from math import fabs

def int_to_string(x: int) -> str:
    if x == 0:
        return "0"

    l = deque()
    sign = int(fabs(x) // x)
    if sign == -1:
        x *= sign

    while x:
        l.appendleft(str(x%10))
        x //= 10

    if sign == -1:
        l[0] = "-" + l[0]

    return "".join(l)


def string_to_int(s: str) -> int:
    nums = list(s)
    sign = 1
    result = 0
    isSignPresentInStart = False
    if len(s) != 0:
        if nums[0] == "-":
            sign = -1
            isSignPresentInStart = True
        elif nums[0] == "+":
            isSignPresentInStart = True

        if isSignPresentInStart:
            nums = nums[1:]

        for i,num in enumerate(reversed(nums)):
            result += (ord(num) - ord("0")) * (10 ** i)

    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    # print(int_to_string(123566))
    # print(int_to_string(-123))
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
