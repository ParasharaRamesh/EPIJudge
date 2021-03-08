from typing import Optional

from EPIJudge.epi_judge_python.remove_duplicates_from_sorted_list import get_length
from list_node import ListNode
from test_framework import generic_test
from delete_kth_last_from_list import *

def getLastNode(L):
    end = L
    prev = None
    while end.next:
        prev = end
        end = end.next
    return end

def cyclically_right_shift_list_naive(L: ListNode, k: int) -> Optional[ListNode]:
    if L == None:
        return None
    if k == 0:
        return L
    if L.next == None:
        return L

    beg = L
    end = getLastNode(beg)

    for i in range(k):
        lastNodeValue = end.data
        curr = beg
        while curr.next:
            dataToWriteInCurrIteration = curr.data
            dataToWrite = curr.next.data
            curr.next.data = dataToWrite


            curr = curr.next
        beg.data = lastNodeValue

    return beg

def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if L == None:
        return None
    if L.next == None:
        return L

    length = get_length(L)
    shiftAmount = k % length
    if shiftAmount == 0:
        return L

    newHead = get_kth_last_node(L, shiftAmount)
    #go to the end and point the next of last node to beg
    curr = newHead
    while curr.next:
        curr = curr.next
    #now curr is the last node
    curr.next = L

    #go till the curr.next is newHead and disconnect it
    curr = L
    while id(curr.next) != id(newHead):
        curr = curr.next

    curr.next = None

    return newHead



if __name__ == '__main__':
    # d = ListNode(4,None)
    # c = ListNode(3,d)
    # b = ListNode(2,c)
    # a = ListNode(1,b)
    # print(cyclically_right_shift_list(a, 9))
    exit(generic_test.generic_test_main('list_cyclic_right_shift.py','list_cyclic_right_shift.tsv',cyclically_right_shift_list))
