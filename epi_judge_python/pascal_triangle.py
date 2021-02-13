from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    pascal = [[1]]
    for i in range(1,n):
        pascal.append([])
        #modify that based on prev row
        for j in range(len(pascal[i-1]) + 1):
            if j == 0 or j == len(pascal[i-1]):
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j] + pascal[i-1][j-1])

    return pascal


if __name__ == '__main__':
    # print(generate_pascal_triangle(15))
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
