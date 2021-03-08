import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if l == None:
        return None

    lesserHead = lesserTail = None
    equalHead = equalTail = None
    higherHead = higherTail = None

    curr = l
    while curr:
        after = curr.next
        curr.next = None

        if curr.data < x:
            if lesserHead == None:
                lesserHead = lesserTail = curr
            else:
                lesserTail.next = curr
                lesserTail = curr
        elif curr.data == x:
            if equalHead == None:
                equalHead = equalTail = curr
            else:
                equalTail.next = curr
                equalTail = curr
        else:
            if higherHead == None:
                higherHead = higherTail = curr
            else:
                higherTail.next = curr
                higherTail = curr
        curr = after

    #do the connections
    if lesserTail:
        if equalHead:
            lesserTail.next = equalHead
            equalTail.next = higherHead
        elif higherHead:
            lesserTail.next = higherHead
        return lesserHead
    elif equalTail:
        if higherHead:
            equalTail.next = higherHead
        return equalHead
    elif higherTail:
        return higherHead

def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',list_pivoting_wrapper))
