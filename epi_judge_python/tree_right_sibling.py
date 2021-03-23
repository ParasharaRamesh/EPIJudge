import functools
from collections import deque
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.

def binary_tree_depth_order_with_next_nodes(tree: BinaryTreeNode) -> List[List[BinaryTreeNode]]:
    depthQueue = deque([])
    depths = []
    if tree:
        depthQueue.append((tree, 1))
        while len(depthQueue) != 0:
            currNode, currHeight = depthQueue.pop()
            if currNode != None:
                if len(depths) < currHeight:
                    depths.append([])
                if len(depths[currHeight - 1]) > 0:
                    depths[currHeight - 1][-1].next = currNode
                depths[currHeight - 1].append(currNode)
                depthQueue.append((currNode.right, currHeight + 1))
                depthQueue.append((currNode.left, currHeight + 1))
    return list(depths)


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    binary_tree_depth_order_with_next_nodes(tree)

def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
