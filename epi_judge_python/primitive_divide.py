from test_framework import generic_test

def findNearest2Multiple(x, y):
    noOfShiftsNeeded = 0
    while x > (y << noOfShiftsNeeded):
        noOfShiftsNeeded +=1
    return noOfShiftsNeeded - 1

def util(x, y, q):
    if x < y:
        return q
    if x == y:
        return q+1

    #find nearest multiple of y in powers of 2 lesser than x
    noOfShiftsNeeded = findNearest2Multiple(x, y)
    return util(x-(y << noOfShiftsNeeded), y, q + (1<< noOfShiftsNeeded))


def divide(x: int, y: int) -> int:
    return util(x, y , 0)



if __name__ == '__main__':
    # print(28847325//1260)
    # print(divide(456,5))
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
