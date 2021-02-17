from typing import List

from test_framework import generic_test

def isValidSubIpRange(subRange: str):
    isLengthValid = 1 <= len(subRange) <= 3
    isValidNumber = len(subRange) >= 1 and 0 < int(subRange) <= 255 and int(subRange[0]) > 0
    isValidZero = len(subRange) == 1 and int(subRange) == 0

    return isLengthValid and (isValidNumber or isValidZero)

# 0.0.0.0 -> 255.255.255.255
def util(currSWithDots, leftOverS, no_of_remaining_dots, valid_ips):
    if no_of_remaining_dots == 0 or len(leftOverS) == 0:
        return
    else:
        minRemainingLimit = no_of_remaining_dots
        maxRemainingLimit = no_of_remaining_dots * 3
        for i in range(1, 4):
            beforeDot = leftOverS[0:i]
            afterDot = leftOverS[i:]
            if isValidSubIpRange(beforeDot) and minRemainingLimit <= len(afterDot) <= maxRemainingLimit:
                curr = currSWithDots + f"{beforeDot}."
                left = afterDot[:]
                if no_of_remaining_dots == 1 and isValidSubIpRange(beforeDot) and isValidSubIpRange(afterDot):
                    valid_ip = f"{curr}{left}"
                    valid_ips.append(valid_ip)

                util(curr, left, no_of_remaining_dots - 1, valid_ips)

def get_valid_ip_address(s: str) -> List[str]:
    valid_ips = []
    no_of_remaining_dots = 3
    util("", s, no_of_remaining_dots,valid_ips)
    return valid_ips


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    # print(isValidSubIpRange("0"))
    # print(isValidSubIpRange("000"))
    # print(isValidSubIpRange("001"))
    # print(isValidSubIpRange("01"))
    # print(isValidSubIpRange("12"))
    # print(isValidSubIpRange("125"))
    # print(isValidSubIpRange("255"))
    # print(isValidSubIpRange("256"))
    # print(isValidSubIpRange("256"))
    # print(isValidSubIpRange("812"))
    # print(isValidSubIpRange("8122"))
    # print(isValidSubIpRange("010"))
    # print(isValidSubIpRange("023"))

    # expected: ['1.8.8.212', '1.8.82.12', '1.88.2.12', '1.88.21.2', '18.8.2.12', '18.8.21.2', '18.82.1.2', '188.2.1.2']
    # print(get_valid_ip_address("188212"))

    # print(get_valid_ip_address("11000"))
    # print(get_valid_ip_address("99220136"))

    exit(generic_test.generic_test_main('valid_ip_addresses.py', 'valid_ip_addresses.tsv', get_valid_ip_address,comparator=comp))
