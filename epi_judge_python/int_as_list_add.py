from typing import Optional

from EPIJudge.epi_judge_python.remove_duplicates_from_sorted_list import get_length
from list_node import ListNode
from test_framework import generic_test
from math import *


def appendZereos(l, diff):
    curr = l
    # go the last node
    while curr.next:
        curr = curr.next
    #add zeroes
    for i in range(diff):
        zeroNode = ListNode(0)
        curr.next = zeroNode
        curr = zeroNode
    return


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    a = L1
    b = L2
    resultHead = resultTail = None
    carry = 0

    l1 = get_length(L1)
    l2 = get_length(L2)
    diff = l1-l2

    if diff > 0:
        appendZereos(L2, diff)
    elif diff < 0:
        appendZereos(L1, -diff)

    while a:
        sum = a.data + b.data + carry

        data = sum % 10
        carry = sum // 10

        dataNode = ListNode(data)

        if resultHead == None:
            resultHead = resultTail = dataNode
        else:
            resultTail.next = dataNode
            resultTail = dataNode

        a = a.next
        b = b.next

    if carry > 0:
        carryNode = ListNode(carry)
        resultTail.next = carryNode
        resultTail = carryNode

    return resultHead


if __name__ == '__main__':
    # a4 = ListNode(1,None)
    # a3 = ListNode(1,a4)
    # a2 = ListNode(2,a3)
    # a1 = ListNode(1,None)

    # b3 = ListNode(1,None)
    # b2 = ListNode(2,b3)
    # b1 = ListNode(9,None)

    # print(add_two_numbers(a1,b1))
    exit(generic_test.generic_test_main('int_as_list_add.py','int_as_list_add.tsv', add_two_numbers))
