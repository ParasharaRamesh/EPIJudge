from test_framework import generic_test


def compute(a, b, op):
    if op == "+":
        return str(int(a) + int(b))
    elif op == "-":
        return str(int(a) - int(b))
    elif op == "*":
        return str(int(a) * int(b))
    else:
        return str(int(a) // int(b))


def isNumeric(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def evaluate(expression: str) -> int:
    ops = expression.split(",")
    opsStack = []
    for op in ops:
        if isNumeric(op):
            opsStack.append(op)
        else:
            # take the top two and evaluate and put it back in
            b = opsStack.pop(-1)
            a = opsStack.pop(-1)
            val = compute(a, b, op)
            opsStack.append(val)

    return int(opsStack.pop())


if __name__ == '__main__':
    # print(evaluate("-641,6,/,28,/"))
    exit(generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',evaluate))
