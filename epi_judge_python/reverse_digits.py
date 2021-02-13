from test_framework import generic_test
import math

def reverse(x: int) -> int:
    # TODO - you fill in here.
    r = []
    abs = int(math.fabs(x))
    sign = abs//x
    while abs > 0:
        r.append(abs%10)
        abs//=10
    ans = 0
    for i,k in enumerate(reversed(r)):
        ans += k * 10**i

    return int(ans*sign)


if __name__ == '__main__':
    # print(reverse(-1856396381))
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
