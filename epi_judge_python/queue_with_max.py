from collections import deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self.Q = deque()
        self.maxCandidates = deque()

    def enqueue(self, x: int) -> None:
        self.Q.append(x)
        #make sure that for this element put in candidates
        while self.maxCandidates and self.maxCandidates[-1] < x:
            self.maxCandidates.pop()
        self.maxCandidates.append(x)

    def dequeue(self) -> int:
        dequed = self.Q.popleft()
        if dequed == self.maxCandidates[0]:
            self.maxCandidates.popleft()
        return dequed

    def max(self) -> int:
        if self.Q:
            return self.maxCandidates[0]
        return 0


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
