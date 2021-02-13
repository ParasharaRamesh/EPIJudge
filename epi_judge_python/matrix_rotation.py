from typing import List

from test_framework import generic_test


def get_in_place_transpose(square_matrix):
    n = len(square_matrix)
    for i in range(n):
        for j in range(i, n):
            square_matrix[i][j], square_matrix[j][i] = square_matrix[j][i], square_matrix[i][j]
    return

def reverse_each_row(square_matrix):
    for i,row in enumerate(square_matrix):
        square_matrix[i].reverse()
    return

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    get_in_place_transpose(square_matrix)
    reverse_each_row(square_matrix)
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,2],[3,4]]
    # mat = []
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # get_in_place_transpose(mat)
    # print(mat)
    # reverse_each_row(mat)
    # print(mat)

