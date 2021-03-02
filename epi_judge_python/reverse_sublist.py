from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverseListRecursive(head):
    if head == None:
        return None
    if head.next == None:
        return head

    reverseList(head.next)
    head.next.next = head
    head.next = None
    return


def reverseListIterative(head):
    if head == None:
        return None
    if head.next == None:
        return head

    previous = None
    curr = head
    next = head.next

    while next:
        #do the reversal
        curr.next = previous

        previous = curr
        curr = next
        next = next.next
    #for the last node
    curr.next = previous
    return

def reverseList(head, recursive = True):
    if recursive:
        reverseListRecursive(head)
    else:
        reverseListIterative(head)



def getNodes(head, start, finish):
    curr = 1
    beforeStart = start - 1
    afterFinish = finish + 1

    beforeStartNode = None
    startNode = None
    finishNode = None
    afterFinishNode = None

    #only for valid indices
    if start >=1 and finish >= 1:
        while head:
            if beforeStart >= 1 and curr == beforeStart:
                beforeStartNode = head
            if start >= 1 and curr == start:
                startNode = head
            if finish >= 1 and curr == finish:
                finishNode = head
            if afterFinish >= 1 and curr == afterFinish:
                afterFinishNode = head
                #no need to process anymore
                break
            head = head.next
            curr += 1
    return beforeStartNode, startNode, finishNode, afterFinishNode


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    head = L
    beforeStartNode, startNode, finishNode, afterFinishNode = getNodes(L, start, finish)

    if beforeStartNode == None and startNode == None and finishNode == None and afterFinishNode == None:
        return L
    else:
        # break the connection
        finishNode.next = None
        reverseList(startNode, False)
        # do the subreversal connection
        if beforeStartNode != None:
            beforeStartNode.next = finishNode
        startNode.next = afterFinishNode

        #beforeStartNode is the new start node
        if beforeStartNode!= None and start - 1 == 1:
            return beforeStartNode
        elif beforeStartNode == None and start == 1 and finishNode!=None:
            return finishNode
        elif start-1 > 1:
            return head


if __name__ == '__main__':
    # testing reverse
    # e = ListNode(5, None)
    # d = ListNode(4, e)
    # c = ListNode(3, d)
    # b = ListNode(2, c)
    # a = ListNode(1, b)

    # print(f"before reversal {a}")
    # reverseList(a)
    # print(f"after reversal {e}")

    # testing getting the nodes
    # print(getNodes(a,1,1))
    # print(getNodes(a,1,2))
    # print(getNodes(a,2,4))
    # print(getNodes(a,0,4))

    # test everything
    # print(reverse_sublist(a, 1,1))
    # print(reverse_sublist(a, 1,5))
    # print(reverse_sublist(a, 1,2))

    # all standard test cases
    exit(generic_test.generic_test_main('reverse_sublist.py','reverse_sublist.tsv', reverse_sublist))
