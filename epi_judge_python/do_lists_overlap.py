import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from is_list_cyclic import get_cycle_if_present
from do_terminated_lists_overlap import overlapping_no_cycle_lists


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    s0, L0 = get_cycle_if_present(l0)
    s1, L1 = get_cycle_if_present(l1)
    # if one has cycle and the other doesnt then they dont meet
    if (s0 == None and s1 != None) or (s0 != None and s1 == None):
        return None
    # if both of them dont have cycles reuse the previous implementation
    if s0 == None and s1 == None:
        return overlapping_no_cycle_lists(l0,l1)
    # if both of them have cycles of different lengths they dont meet
    if L0 != L1:
        return None
    # if both of them have cycles of same lengths then get the starting points of both and see if they ever match
    if L0 == L1:
        i = 1
        curr = s0
        while i <= L1 and id(curr) != id(s1):
            curr = curr.next
            i+=1

        if id(curr) == id(s1):
            #if they match while traversing in the cycle
            return curr
        elif i == L1:
            return None

@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
