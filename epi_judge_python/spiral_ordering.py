from typing import List
from math import ceil
from test_framework import generic_test


def noOfElements(n):
    if n == 1:
        return 1
    return 4 * (n - 1)


def keepWalkingRight(grid, n, subGridSize):
    right = []
    diff = (n - subGridSize)//2
    start = (diff, diff)
    y = start[1]
    while True:
        if y - start[1] < subGridSize:
            curr = grid[start[0]][y]
            right.append(curr)
            y +=1
        else:
            break
    return right

def keepWalkingDown(grid, n, subGridSize):
    down = []
    diff = (n - subGridSize)//2
    start = (diff+1, n-1-diff)
    x = start[0]
    while True:
        if x - start[0] < subGridSize -1:
            curr = grid[x][start[1]]
            down.append(curr)
            x += 1
        else:
            break
    return down

def keepWalkingLeft(grid, n, subGridSize):
    left = []
    diff = (n - subGridSize)//2
    start = (n-1-diff,n-2-diff)
    negy = start[1]
    while True:
        if start[1] - negy < subGridSize -1:
            curr = grid[start[0]][negy]
            left.append(curr)
            negy -=1
        else:
            break
    return left

def keepWalkingUp(grid, n, subGridSize):
    up = []
    diff = (n - subGridSize)//2
    start = (n-2-diff, diff)
    negx = start[0]
    while True:
        if start[0] - negx < subGridSize -2:
            curr = grid[negx][start[1]]
            up.append(curr)
            negx -= 1
        else:
            break
    return up

def walkLevel(n, subGridSize, spiral, grid):
    # go right , go down , go left, go up
    right = keepWalkingRight(grid, n, subGridSize)
    down = keepWalkingDown(grid, n, subGridSize)
    left = keepWalkingLeft(grid, n, subGridSize)
    up = keepWalkingUp(grid, n, subGridSize)
    return spiral + right + down + left + up


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    levels = int(ceil(n / 2))
    i = levels
    spiral = []
    j = 0
    # start from outermost level and then go inside
    while i > 0:
        spiral = walkLevel(n, n - j, spiral, square_matrix)
        j += 2
        i-=1
    return spiral


if __name__ == '__main__':
    # print(matrix_in_spiral_order([]))
    # print(matrix_in_spiral_order([[1]]))
    # print(matrix_in_spiral_order([[1,2],[4,3]]))
    # print(matrix_in_spiral_order([[1,2,3],[8,9,4],[7,6,5]]))
    # print(matrix_in_spiral_order([[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]))
    # print(matrix_in_spiral_order([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
    exit(generic_test.generic_test_main('spiral_ordering.py','spiral_ordering.tsv',matrix_in_spiral_order))
