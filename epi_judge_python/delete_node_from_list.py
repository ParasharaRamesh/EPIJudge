import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assumes node_to_delete is not tail.
def deletion_from_list_naive(node_to_delete: ListNode) -> None:
    curr = node_to_delete
    while curr.next.next:
        after = curr.next
        if after:
            curr.data = after.data
        curr = after
    #copy last
    curr.data = curr.next.data
    #delete last node
    curr.next = None
    return

def deletion_from_list(node_to_delete: ListNode) -> None:
    curr = node_to_delete
    curr.data = curr.next.data
    curr.next = curr.next.next

@enable_executor_hook
def deletion_from_list_wrapper(executor, head, node_to_delete_idx):
    node_to_delete = head
    if node_to_delete is None:
        raise RuntimeError('List is empty')
    for _ in range(node_to_delete_idx):
        if node_to_delete.next is None:
            raise RuntimeError('Can\'t delete last node')
        node_to_delete = node_to_delete.next

    executor.run(functools.partial(deletion_from_list, node_to_delete))

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_node_from_list.py',
                                       'delete_node_from_list.tsv',
                                       deletion_from_list_wrapper))
