from typing import List
import math
from test_framework import generic_test

def multiplyListWithNum(l , num):

    if num == 0:
        return [0]

    r = list(reversed(l))
    carry = 0

    for i in range(len(r)):
        mul = int(math.fabs(r[i] * num)) + carry
        if mul > 9:
            carry = (mul //10)%10
            unitsDigit = mul %10
            r[i] = unitsDigit
        else:
            r[i] = mul
            carry = 0

    if carry > 0:
        r.append(carry)

    ans = list(reversed(r))
    return ans


def addTwoNumLists(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    diff = int(math.fabs(n1 - n2))
    #match the two lists
    if n1 > n2:
        l2 = list(reversed(l2))
        l2.extend([0]*diff)
        l1 = list(reversed(l1))
    elif n1 < n2:
        l1 = list(reversed(l1))
        l1.extend([0]* diff)
        l2 = list(reversed(l2))
    else:
        l1 = list(reversed(l1))
        l2 = list(reversed(l2))

    #now to add both
    carry = 0
    res =  [0]* n2 if n1 < n2 else [0]*n1

    for i, x in enumerate(zip(l1, l2)):
        a,b = x
        add = a+b+ carry
        if add > 9:
            carry = (add //10) % 10
            sum = add%10
            res[i] = sum
        else:
            carry = 0
            res[i] = add
    if carry > 0:
        res.append(carry)

    return list(reversed(res))




def multiply(num1: List[int], num2: List[int]) -> List[int]:
    res = []
    n1 = len(num1)
    n2 = len(num2)

    x = num1[0] * num2[0]
    sign = 0 if x == 0 else int(int(math.fabs(x)) / x)

    if n1 < n2:
        num1, num2 = num2, num1

    for level,n in enumerate(reversed(num2)):
        mulList = multiplyListWithNum(num1, n)
        mulList.extend([0]*level)
        res = addTwoNumLists(res, mulList)

    res[0]*=sign

    return res

if __name__ == '__main__':
    # print(multiplyListWithNum([2,5],5))
    # print(multiplyListWithNum([2,5],2))
    # print(addTwoNumLists([2,5],[9,0]))
    # print(multiply([0],[-1,0,0,0]))
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
