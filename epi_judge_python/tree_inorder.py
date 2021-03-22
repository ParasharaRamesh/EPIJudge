from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def inorder_recursive(tree, inorderList):
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
    stackFrames = []
    stackFrames.append([tree, 0])
    while stackFrames:
        currNode, currState = stackFrames[-1]

        if currNode == None or currState == 3:
            stackFrames.pop()
        elif currState == 0:
            stackFrames[-1][1] += 1
            stackFrames.append([currNode.left, 0])
        elif currState == 1:
            stackFrames[-1][1] += 1
            inorderList.append(currNode.data)
        elif currState == 2:
            stackFrames[-1][1] += 1
            stackFrames.append([currNode.right, 0])

    return inorderList

if __name__ == '__main__':
    # c = BinaryTreeNode(3,None, None)
    # b = BinaryTreeNode(2,None, None)
    # a = BinaryTreeNode(1,b, c)
    # print(inorder_traversal(a))
    exit(generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv', inorder_traversal))
