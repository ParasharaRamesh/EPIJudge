from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],inorder: List[int]) -> BinaryTreeNode:
    if len(preorder) > 0:
        if len(preorder) == len(inorder) == 1:
            return BinaryTreeNode(preorder[0])

        rootData = preorder[0]
        indexInInorder = inorder.index(rootData)

        leftPreOrder = preorder[1: indexInInorder + 1]
        leftInOrder = inorder[: indexInInorder]
        rightPreOrder = preorder[indexInInorder + 1 :]
        rightInOrder = inorder[indexInInorder + 1: ]
        leftSubTree = binary_tree_from_preorder_inorder(leftPreOrder, leftInOrder)
        rightSubTree = binary_tree_from_preorder_inorder(rightPreOrder, rightInOrder)

        return BinaryTreeNode(rootData, leftSubTree, rightSubTree)
    return None


if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_from_preorder_inorder.py','tree_from_preorder_inorder.tsv',binary_tree_from_preorder_inorder))
