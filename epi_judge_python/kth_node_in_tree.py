import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,k: int) -> Optional[BinaryTreeNode]:
    if tree:
        if tree.left == None and tree.right == None and k == 1:
            return tree
        elif tree.left:
            leftSize = tree.left.size
            if leftSize + 1 == k:
                return tree
            elif leftSize + 1 > k:
                # do something with left tree
                return find_kth_node_binary_tree(tree.left, k)
            elif leftSize + 1 < k:
                # do something with right tree
                return find_kth_node_binary_tree(tree.right, k - leftSize - 1)
        elif tree.right:
            if k == 1:
                return tree
            else:
                # do something with right tree
                return find_kth_node_binary_tree(tree.right, k - 1)

    return None


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
