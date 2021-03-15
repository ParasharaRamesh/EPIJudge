from functools import reduce

from EPIJudge.epi_judge_python.convert_base import convert_base
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sumOfBinaries(binaries):
    sum = 0
    for binary in binaries:
        sum += int(convert_base(binary, 2, 10))
    return sum

def get_all_numbers_from_leaves(tree: BinaryTreeNode, path: str, allBinaries: [str]) -> [str]:
    if tree:
        if tree.left == None and tree.right == None:
            allBinaries.append(path + str(tree.data))

        get_all_numbers_from_leaves(tree.left, path + str(tree.data), allBinaries)
        get_all_numbers_from_leaves(tree.right, path + str(tree.data), allBinaries)

    return allBinaries


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    allBinaries = []
    get_all_numbers_from_leaves(tree, "", allBinaries)
    return sumOfBinaries(allBinaries)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('sum_root_to_leaf.py', 'sum_root_to_leaf.tsv', sum_root_to_leaf))
