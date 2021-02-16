# from typing import List
#
# from test_framework import generic_test
#
#
# # 0.0.0.0 -> 255.255.255.255
# def util(currSWithDots, leftOverS, no_of_remaining_dots, valid_ips):
#     if no_of_remaining_dots == 0 or len(leftOverS) == 0:
#         return
#     else:
#         minRemainingLimit = no_of_remaining_dots + 1
#         maxRemainingLimit = no_of_remaining_dots * 3
#         for i in range(1, 4):
#             beforeDot = leftOverS[0:i]
#             afterDot = leftOverS[i:]
#             if len(beforeDot) > 0 and len(afterDot) > 0 and int(beforeDot) == 0 and int(afterDot) == 0 and len(leftOverS) > 2:
#                 return
#             elif len(leftOverS) == no_of_remaining_dots + 1:
#                 leftOverSWithDots = list(leftOverS)
#                 insertIndex = 1
#                 for i in range(no_of_remaining_dots):
#                     leftOverSWithDots.insert(insertIndex, ".")
#                     insertIndex += 2
#                 valid_ips.append(f"{currSWithDots}{''.join(leftOverSWithDots)}")
#                 return
#             elif len(leftOverS) == (no_of_remaining_dots + 1) * 3:
#                 leftOverSWithDots = list(leftOverS)
#                 insertIndex = 3
#                 for i in range(no_of_remaining_dots):
#                     if leftOverSWithDots[insertIndex - 3] == 0:
#                         return
#                     leftOverSWithDots.insert(insertIndex, ".")
#                     insertIndex += 4
#                 valid_ips.append(f"{currSWithDots}{''.join(leftOverSWithDots)}")
#                 return
#             elif int(beforeDot) <= 255 and minRemainingLimit <= len(leftOverS) and len(afterDot) <= maxRemainingLimit:
#                 if len(beforeDot) == 1 and int(beforeDot) == 0:
#                     if len(afterDot) > 1 and int(afterDot) > 0:
#                         curr = currSWithDots + f"{beforeDot}."
#                         left = afterDot[:]
#                         util(curr, left, no_of_remaining_dots - 1, valid_ips)
#                     elif len(afterDot) == 1:
#                         valid_ip = f"{currSWithDots}{beforeDot}.{afterDot}"
#                         valid_ips.append(valid_ip)
#                         return
#                 elif no_of_remaining_dots > 1:
#                     curr = currSWithDots + f"{beforeDot}."
#                     left = afterDot[:]
#                     util(curr, left, no_of_remaining_dots - 1, valid_ips)
#                 elif len(afterDot) > 0 and int(afterDot) <= 255 and len(beforeDot) <= minRemainingLimit:
#                     if int(afterDot) > 0 or (int(afterDot) == 0 and len(afterDot) == 1):
#                         curr = currSWithDots + f"{beforeDot}."
#                         left = afterDot[:]
#                         valid_ip = f"{curr}{left}"
#                         valid_ips.append(valid_ip)
#                         util(curr, left, no_of_remaining_dots - 1, valid_ips)
#
#         return
#
#
# def get_valid_ip_address(s: str) -> List[str]:
#     valid_ips = []
#     no_of_remaining_dots = 3
#     util("", s, no_of_remaining_dots,valid_ips)
#     return valid_ips
#
#
# def comp(a, b):
#     return sorted(a) == sorted(b)
#
#
# if __name__ == '__main__':
#     # missing a few ips!
#     # expected: ['1.8.8.212', '1.8.82.12', '1.88.2.12', '1.88.21.2', '18.8.2.12', '18.8.21.2', '18.82.1.2', '188.2.1.2']
#     # print(get_valid_ip_address("188212"))
#     # print(get_valid_ip_address("11000"))
#     print(get_valid_ip_address("99220136"))
#     exit(generic_test.generic_test_main('valid_ip_addresses.py', 'valid_ip_addresses.tsv', get_valid_ip_address,comparator=comp))
