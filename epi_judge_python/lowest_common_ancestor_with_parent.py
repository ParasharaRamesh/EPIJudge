import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from lowest_common_ancestor import isNodePresent


def lca_with_parent_naive(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    #one of it is the root
    if node0.parent == None:
        return node0
    if node1.parent == None:
        return node1

    currLeft, currRight = node0, node1

    while currLeft != currRight:
        isRightInLeft = isNodePresent(currRight,currLeft)
        isLeftInRight = isNodePresent(currLeft,currRight)

        if isRightInLeft and not isLeftInRight:
            return currLeft
        if isLeftInRight and not isRightInLeft:
            return currRight

        currLeft = currLeft.parent
        currRight = currRight.parent


    return currLeft

def getDepthWithParentPointers(node):
    curr = node
    depth = 0
    while curr:
        curr = curr.parent
        depth += 1
    return depth


def traverseUpwards(node, toTraverse):
    curr = node
    for i in range(toTraverse):
        curr = curr.parent
    return curr


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    depth0 = getDepthWithParentPointers(node0)
    depth1 = getDepthWithParentPointers(node1)
    diff = depth0 - depth1

    curr0 = node0
    curr1 = node1

    if diff > 0:
        curr0 = traverseUpwards(curr0, diff)
    elif diff < 0:
        curr1 = traverseUpwards(curr1, -diff)

    while curr0 and curr1 and curr0 != curr1:
        curr0 = curr0.parent
        curr1 = curr1.parent
    return curr0

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(generic_test.generic_test_main('lowest_common_ancestor_with_parent.py', 'lowest_common_ancestor.tsv',lca_wrapper))
