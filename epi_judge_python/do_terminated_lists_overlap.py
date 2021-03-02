import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def getLength(l):
    curr = l
    l = 0
    while curr:
        curr = curr.next
        l+=1
    return l

def getNode(l, d):
    curr = l
    i = 0
    while curr and i<d:
        curr = curr.next
        i+=1
    if i < d:
        return None
    return curr

def walkTogether(currA,currB):
    while currA != currB:
        currA = currA.next
        currB = currB.next
    if currA == None:
        return None
    else:
        return currA

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    a = getLength(l0)
    b = getLength(l1)

    diff = a-b
    if diff > 0:
        #a is the longer list, go diff + 1 in a , go diff in b and compare
        currA = getNode(l0, diff)
        currB = l1
    elif diff < 0:
        #b is the longer list, go diff + 1 in b , go diff in a and compare
        currA = l0
        currB = getNode(l1, -1 * diff)
    else:
        #do one by one traversal until we see a common node
        currA = l0
        currB = l1
    return walkTogether(currA, currB)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('do_terminated_lists_overlap.py','do_terminated_lists_overlap.tsv',overlapping_no_cycle_lists_wrapper))
