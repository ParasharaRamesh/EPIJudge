from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def recursiveHelper(tree, currHeight, depths):
    if tree == None:
        return

    if len(depths) < currHeight:
        depths.append([])

    depths[currHeight-1].append(tree.data)

    recursiveHelper(tree.left, currHeight + 1, depths)
    recursiveHelper(tree.right, currHeight + 1, depths)

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    depths = []
    recursiveHelper(tree, 1, depths)
    return depths


if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_level_order.py','tree_level_order.tsv', binary_tree_depth_order))
