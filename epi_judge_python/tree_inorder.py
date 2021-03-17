from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_recursive(tree,inorderList):
    if tree:
        inorder_recursive(tree.left, inorderList)
        inorderList.append(tree.data)
        inorder_recursive(tree.right, inorderList)

def inorder_traversal_recursive(tree: BinaryTreeNode) -> List[int]:
    inorderList = []
    inorder_recursive(tree, inorderList)
    return inorderList

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    inorderList = []
    #TODO
    return inorderList

if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',inorder_traversal))
