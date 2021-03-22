from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from successor_in_tree import *

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    inorder = []
    leftMost = leftMostNode(tree)

    curr = leftMost
    inorder.append(curr.data)
    while True:
        successor = find_successor(curr)
        if successor:
            inorder.append(successor.data)
            curr = successor
        else:
            break

    return inorder


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
