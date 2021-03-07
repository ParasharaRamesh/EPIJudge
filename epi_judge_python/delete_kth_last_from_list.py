from typing import Optional
from delete_node_from_list import *
from list_node import ListNode
from test_framework import generic_test

# NOTE: can use deletion_from_list(node)
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    curr = L
    afterK = None
    i = 1
    while i<=k:
        curr = curr.next
        i+=1

    beforeK = L
    afterK = curr

    while afterK:
        beforeK = beforeK.next
        afterK = afterK.next

    if k > 1:
        deletion_from_list(beforeK)
        return L
    else:
        curr = L
        if curr.next:
            while curr.next.next:
                curr = curr.next
            curr.next = None
            return L
        else:
            return None

if __name__ == '__main__':
    # b = ListNode(1,None)
    # a = ListNode(2,b)
    # remove_kth_last(a, 1)
    exit(generic_test.generic_test_main('delete_kth_last_from_list.py','delete_kth_last_from_list.tsv',remove_kth_last))
