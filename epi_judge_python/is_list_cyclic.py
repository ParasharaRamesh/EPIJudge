import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_cycle_if_present(head):
    # base cases
    if head == None:
        # nothing
        return None, 0
    if head.next == None:
        # one element
        return None, 0

    # get the meeting point
    slow = head
    fast = head.next
    meet = None
    while id(slow) != id(fast):
        if slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        else:
            # it is a singly linked list
            return None, 0
    # set meeting point
    meet = slow

    # get the length of the loop L
    curr = meet.next
    L = 1
    while id(curr) != id(meet):
        curr = curr.next
        L += 1

    # have two pointers
    start = afterL = head
    i = 0
    while i < L:
        afterL = afterL.next
        i += 1

    # move start and afterL one by one until they match
    while id(start) != id(afterL):
        start = start.next
        afterL = afterL.next

    return start, L


# None if there is no cycle
# node at start of the cycle if cycle is present
def has_cycle(head: ListNode) -> Optional[ListNode]:
    start, L = get_cycle_if_present(head)
    return start


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(generic_test.generic_test_main('is_list_cyclic.py', 'is_list_cyclic.tsv', has_cycle_wrapper))
