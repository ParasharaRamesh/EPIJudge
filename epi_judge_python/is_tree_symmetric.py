from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def checkMirrorNodes(leftNode, rightNode):
    if leftNode == None and rightNode == None:
        return True

    isDataEqual = leftNode != None and rightNode != None and leftNode.data == rightNode.data
    return isDataEqual and checkMirrorNodes(leftNode.right, rightNode.left) and checkMirrorNodes(leftNode.left, rightNode.right)



def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree:
        return checkMirrorNodes(tree.left, tree.right)
    return True

if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_tree_symmetric.py','is_tree_symmetric.tsv', is_symmetric))
