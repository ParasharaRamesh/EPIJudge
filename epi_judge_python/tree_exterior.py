import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from tree_connect_leaves import *

def isNodeALeaf(node):
    if node:
        return node.left == None and node.right == None
    return False

def computeLeftExterior(tree):
    leftExterior = []
    curr = tree
    while curr and not isNodeALeaf(curr):
        leftExterior.append(curr)
        if curr.left:
            curr = curr.left
        elif curr.right:
            curr = curr.right
        else:
            break
    return leftExterior

def computeRightExterior(tree):
    rightExterior = []
    curr = tree
    while curr and not isNodeALeaf(curr):
        rightExterior.append(curr)
        if curr.right:
            curr = curr.right
        elif curr.left:
            curr = curr.left
        else:
            break
    return rightExterior

def computeExterior(tree):
    if tree:
        leftExteriorExcludingLeavesAndParent = computeLeftExterior(tree.left)
        rightExteriorExcludingLeavesAndParent = computeRightExterior(tree.right)
        leaves = create_list_of_leaves(tree)
        exteriorWithoutRoot = leftExteriorExcludingLeavesAndParent + leaves + list(reversed(rightExteriorExcludingLeavesAndParent))
        return exteriorWithoutRoot if isNodeALeaf(tree) else [tree] + exteriorWithoutRoot
    return []

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    exterior = computeExterior(tree)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))
    return create_output_list(result)

if __name__ == '__main__':
    # tree = BinaryTreeNode.constructBinaryTreeFromList([0, -6, 13, 2, -12, None, 3, -6])
    # print(exterior_binary_tree(tree))
    exit(generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',create_output_list_wrapper))
