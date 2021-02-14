from test_framework import generic_test
from string_integer_interconversion import *
from collections import deque

#only positive num in base 10
def convert_list_to_num(num):
    result = 0
    for i,ch in enumerate(reversed(num)):
        result += int(ch) * (10 ** i)
    return result

#num is a list of positive characters
def convert_num_from_some_other_base_to_base_10(num, b1):
    charMapToValue = {chr(ord("A") + i - 10): i for i in range(10, 36)}
    for i in range(10):
        charMapToValue[str(i)] = i

    # convert to base 10 from b1
    base10num = 0
    if b1 == 10:
        # if already in base 10 use it as is
        base10num = convert_list_to_num(num)
    else:
        for i, ch in enumerate(reversed(num)):
            base10num += charMapToValue[ch] * (b1 ** i)
    return base10num

def convert_base_10_to_other_base(num, b2, sign):
    valueToCharMap = {i: chr(ord("A") + i - 10) for i in range(10, 36)}
    for i in range(10):
        valueToCharMap[i] = str(i)
    rems = deque()
    if num > 0:
        while num:
            rems.appendleft(valueToCharMap[num%b2])
            num //= b2
        if sign == -1:
            rems[0] = "-" + rems[0]
        return "".join(rems)
    else:
        return "0"

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    #some edge cases
    if len(num_as_string) == 0:
        return ""
    if b1 == b2:
        return num_as_string

    sign = 1
    result = 0
    num = None
    #take care of sign

    if num_as_string[0] == "-":
        sign = -1
        num = list(num_as_string[1:])
    else:
        num = list(num_as_string)

    base10num = convert_num_from_some_other_base_to_base_10(num, b1)
    if b2 == 10:
        return int_to_string(base10num * sign)

    return convert_base_10_to_other_base(base10num, b2, sign)

if __name__ == '__main__':
    # print(convert_base("0", 3 , 9))
    exit(generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',convert_base))
