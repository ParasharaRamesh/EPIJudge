from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    result = None
    resultHead = None
    print(f"L1 is {L1}")
    print(f"L2 is {L2}")
    currL1 = L1
    currL2 = L2
    while currL1 and currL2:
        currNode = ListNode()
        # populate data based on lower
        if currL1.data <= currL2.data:
            currNode.data = currL1.data
            currL1 = currL1.next
        else:
            currNode.data = currL2.data
            currL2 = currL2.next

        # set the currNode in result list
        if result == None:
            result = resultHead = currNode

        else:
            result.next = currNode
            result = result.next

    # if L1 has reached end then print everything in l2 and viceversa
    if result != None:
        if currL1 == None:
            result.next = currL2
        elif currL2 == None:
            result.next = currL1
    else:
        if currL1 == None:
            return currL2
        elif currL2 == None:
            return currL1
    print(f"Result is {resultHead}")
    return resultHead


if __name__ == '__main__':
    # testing
    # l1b = ListNode(5, None)
    # l1a = ListNode(2, l1b)
    # l1 = ListNode(-1, l1a)
    #
    # l2c = ListNode(7, None)
    # l2b = ListNode(4, l2c)
    # l2a = ListNode(3, l2b)
    # l2 = ListNode(1, l2a)
    #
    # merge_two_sorted_lists(l1, l2)
    exit(generic_test.generic_test_main('sorted_lists_merge.py','sorted_lists_merge.tsv', merge_two_sorted_lists))
