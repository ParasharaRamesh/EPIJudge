import math

from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def constructBinaryTreeFromList(l):
        n = len(l)
        limit = int(math.ceil((n - 3) / 2))
        binaryNodes = []
        for x in l:
            if x is not None:
                binaryNodes.append(BinaryTreeNode(x))
            else:
                binaryNodes.append(None)
        for i in range(limit+1):
            l = 2 * i + 1
            r = 2 * i + 2
            if binaryNodes[i]:
                if l < n:
                    binaryNodes[i].left = binaryNodes[l]
                if r < n:
                    binaryNodes[i].right = binaryNodes[r]
        return binaryNodes[0]
