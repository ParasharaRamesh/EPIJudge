from typing import List

from test_framework import generic_test
from collections import Counter

# Check if a partially filled matrix has any conflicts.
def getRow(grid, i):
    return grid[i]


def isValidInRow(grid, i, j):
    val = grid[i][j]
    row = getRow(grid, i)
    return row.count(val) == 1


def getColumn(grid, j):
    return [grid[x][j] for x in range(len(grid[0]))]


def isValidInColumn(grid, i, j):
    val = grid[i][j]
    column = getColumn(grid, j)
    return column.count(val) == 1


def getSubGridElements(grid, subGridId):
    x = subGridId[0]
    y = subGridId[1]
    subGrid = []
    for i in range(3 * x, 3 * (x + 1)):
        for j in range(3 * y, 3 * (y + 1)):
            subGrid.append(grid[i][j])
    return subGrid

def isValidInSubGrid(grid, i, j):
    val = grid[i][j]
    subGridId = (i // 3, j // 3)
    subGrid = getSubGridElements(grid, subGridId)
    return subGrid.count(val) == 1


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    for i, row in enumerate(partial_assignment):
        for j, val in enumerate(row):
            # if val != 0:
            #     rowValid = isValidInRow(partial_assignment, i, j)
            #     columnValid = isValidInColumn(partial_assignment, i, j)
            #     isSubGridValid = isValidInSubGrid(partial_assignment, i, j)
            #     isValidOverall = rowValid and columnValid and isSubGridValid
            #     if not isValidOverall:
            #         return False
            if val != 0:
                rowCounts = Counter(getRow(partial_assignment, i))
                columnCounts = Counter(getColumn(partial_assignment, j))
                subGridCounts = Counter(getSubGridElements(partial_assignment, (i//3, j//3)))
                rowValid = rowCounts[val] == 1
                columnValid = columnCounts[val] == 1
                isSubGridValid = subGridCounts[val] == 1
                isValidOverall = rowValid and columnValid and isSubGridValid
                if not isValidOverall:
                    return False


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
