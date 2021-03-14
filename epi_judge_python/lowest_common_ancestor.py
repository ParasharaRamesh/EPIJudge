import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def isNodePresent(node: BinaryTreeNode, tree: BinaryTreeNode) -> bool:
    if tree:
        isRootTheNode = node.data == tree.data
        return isRootTheNode or isNodePresent(node, tree.left) or isNodePresent(node, tree.right)
    return False

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if tree:
        isNode0InLeft = isNodePresent(node0, tree.left)
        isNode0InRight = isNodePresent(node0, tree.right)
        isNode1InLeft = isNodePresent(node1, tree.left)
        isNode1InRight = isNodePresent(node1, tree.right)

        if isNode0InLeft and isNode1InLeft:
            return lca(tree.left, node0, node1)

        if isNode0InRight and isNode1InRight:
            return lca(tree.right, node0 , node1)

        return tree

    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(generic_test.generic_test_main('lowest_common_ancestor.py','lowest_common_ancestor.tsv',lca_wrapper))
