from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from math import fabs


def getHeight(node: BinaryTreeNode) -> int:
    if node == None:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if tree:
        leftSubTreeHeight = getHeight(tree.left)
        rightSubTreeHeight = getHeight(tree.right)
        diff = fabs(leftSubTreeHeight - rightSubTreeHeight)
        isThisNodeBalanced = diff <= 1
        return isThisNodeBalanced and is_balanced_binary_tree(tree.left) and is_balanced_binary_tree(tree.right)
    return True

if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_tree_balanced.py','is_tree_balanced.tsv',is_balanced_binary_tree))
