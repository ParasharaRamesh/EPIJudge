from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if L == None or L.next == None or L.next.next == None:
        return L

    evenHead = evenTail = L
    oddHead = oddTail = L.next
    curr = oddTail.next

    evenTail.next = None
    oddTail.next = None

    isEven = True
    while curr:
        after = curr.next
        if isEven:
            evenTail.next = curr
            evenTail = curr
        else:
            oddTail.next = curr
            oddTail = curr
        curr.next = None
        isEven ^= True
        curr = after

    evenTail.next = oddHead
    return evenHead


if __name__ == '__main__':
    # e = ListNode(5,None)
    # d = ListNode(4,e)
    # c = ListNode(3,d)
    # b = ListNode(2,c)
    # a = ListNode(1,b)
    # print(even_odd_merge(a))
    exit(generic_test.generic_test_main('even_odd_list_merge.py','even_odd_list_merge.tsv',even_odd_merge))
