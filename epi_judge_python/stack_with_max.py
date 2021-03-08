from test_framework import generic_test
from test_framework.test_failure import TestFailure
from math import *

class Stack:
    def __init__(self):
        self.stack = []

    def encode(self, ele, max):
        return f"{int(ele)}|{int(max)}"

    def decode(self, val):
        encodings = val.split("|")
        encodings = list(map(lambda x: int(x), encodings))
        return encodings

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        currVal = self.stack[-1]
        _, currMax = self.decode(currVal)
        return currMax

    def pop(self) -> int:
        topVal = self.stack.pop(-1)
        topEle, _ = self.decode(topVal)
        return topEle

    def push(self, x: int) -> None:
        if self.empty():
            self.stack.append(self.encode(x, x))
        else:
            currVal = self.stack[-1]
            _, currMax = self.decode(currVal)
            self.stack.append(self.encode(x, max(x, currMax)))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(generic_test.generic_test_main('stack_with_max.py','stack_with_max.tsv', stack_tester))
