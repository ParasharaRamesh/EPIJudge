from EPIJudge.epi_judge_python.remove_duplicates_from_sorted_list import get_length
from list_node import ListNode
from test_framework import generic_test

def cloneNode(node):
    if node == None:
        return None
    return ListNode(node.data, None)

def reverseCopy(head):
    if head == None:
        return None
    if head.next == None:
        return cloneNode(head)

    previous = None
    curr = head
    next = head.next

    previousCopy = None

    while next:
        currCopy = cloneNode(curr)

        #do the reversal
        currCopy.next = previousCopy

        previous = curr
        previousCopy = currCopy
        curr = next
        next = next.next

    #for the last node
    currCopy = cloneNode(curr)
    currCopy.next = previousCopy
    return currCopy

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if L == None or L.next == None:
        return True

    reverse = reverseCopy(L)
    l = get_length(L)
    toCheck = l//2

    curr = L
    currReverse = reverse

    for i in range(toCheck):
        if curr.data != currReverse.data:
            return False
        curr = curr.next
        currReverse = currReverse.next

    return True


if __name__ == '__main__':
    # testing reverse
    # e = ListNode(5, None)
    # d = ListNode(4, e)
    # c = ListNode(3, d)
    # b = ListNode(2, c)
    # a = ListNode(1, b)
    #
    # print(f"before reversal {a}")
    # print(f"after reversal {reverseCopy(a)}")
    # print(f"after reversal {a}")

    exit(generic_test.generic_test_main('is_list_palindromic.py','is_list_palindromic.tsv', is_linked_list_a_palindrome))
