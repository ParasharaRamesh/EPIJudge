from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque

def recursiveHelper(tree, currHeight, depths):
    if tree == None:
        return

    if len(depths) < currHeight:
        depths.append([])

    depths[currHeight-1].append(tree.data)

    recursiveHelper(tree.left, currHeight + 1, depths)
    recursiveHelper(tree.right, currHeight + 1, depths)

def binary_tree_depth_order_recursive(tree: BinaryTreeNode) -> List[List[int]]:
    depths = []
    recursiveHelper(tree, 1, depths)
    return depths

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    depthQueue = deque([])
    depths = []
    if tree:
        depthQueue.append((tree,1))
        while len(depthQueue) != 0:
            currNode, currHeight = depthQueue.pop()
            if currNode != None:
                if len(depths) < currHeight:
                    depths.append([])
                depths[currHeight-1].append(currNode.data)
                depthQueue.append((currNode.right, currHeight + 1))
                depthQueue.append((currNode.left, currHeight + 1))
    return list(depths)

if __name__ == '__main__':
    exit(generic_test.generic_test_main('tree_level_order.py','tree_level_order.tsv', binary_tree_depth_order))
