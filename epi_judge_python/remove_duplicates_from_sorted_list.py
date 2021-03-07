from typing import Optional

from list_node import ListNode
from test_framework import generic_test

def get_length(L):
    curr = L
    length = 0
    while curr:
        curr = curr.next
        length +=1
    return length

def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    curr = L
    firstOcc = curr
    while curr:
        if curr.data != firstOcc.data:
            firstOcc.next = curr
            firstOcc = curr
        curr = curr.next

    if get_length(firstOcc) > 1:
        firstOcc.next = None

    return L


if __name__ == '__main__':
    # d = ListNode(1,None)
    # c = ListNode(1,d)
    # b = ListNode(1,c)
    # a = ListNode(1,b)
    # remove_duplicates(a)
    exit(generic_test.generic_test_main('remove_duplicates_from_sorted_list.py','remove_duplicates_from_sorted_list.tsv', remove_duplicates))
