import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

'''
        re = re(r1) if re(r1) <= re(r2) else re(r2)
        le = le(r2) if le(r1) <= le(r2) else le(r1)
        be = be(r2) if be(r1) <= be(r2) else be(r1)
        te = te(r2) if te(r1) >= te(r2) else te(r1)
'''


def le(r: Rect):
    return r.x


def re(r: Rect):
    return r.x + r.width


def te(r: Rect):
    return r.y + r.height


def be(r: Rect):
    return r.y


def constructRectWithEdges(l, t, r, b):
    if l | t | r | b == 0:
        return emptyRect()
    return Rect(l, b, r - l, t - b)


def emptyRect():
    return Rect(0, 0, -1, -1)


def getDefaultEdges(r1, r2):
    l = max(le(r1), le(r2))
    t = min(te(r1), te(r2))
    r = min(re(r1), re(r2))
    b = max(be(r1),be(r2))
    return constructRectWithEdges(l=l, t=t, r=r, b=b)

# def isIntersecting(r1,r2):
#     isR2CompletelyInside = le(r2) >= le(r1) and re(r2) <= re(r1) and te(r2) <= te(r1) and be(r2) >= be(r1)
#     isR1CompletelyInside = le(r1) >= le(r2) and re(r1) <= re(r2) and te(r1) <= te(r2) and be(r1) >= be(r2)
#
#     isR2LeftIntersecting  = (le(r2) <= le(r1) <= re(r2) <= re(r1)) and ((te(r2) >= te(r1) >= be(r2) >= be(r1)) or (te(r1) >= te(r2) >= be(r1) >= be(r2)))
#     isR2RightIntersecting = (le(r1) <= le(r2) <= re(r1) <= re(r2)) and ((te(r2) >= te(r1) >= be(r2) >= be(r1)) or (te(r1) >= te(r2) >= be(r1) >= be(r2)))
#     isR2TopIntersecting = (te(r2) >= te(r1) >= be(r2) >= be(r1)) and ((le(r2) <= le(r1) <= re(r2) <= re(r1)) or (le(r1) <= le(r2) <= re(r1) <= re(r2)))
#     isR2BottomIntersecting = (te(r1) >= te(r2) >= be(r1) >= be(r2)) and ((le(r2) <= le(r1) <= re(r2) <= re(r1)) or (le(r1) <= le(r2) <= re(r1) <= re(r2)))
#
#     isR2AcrossWidth = (le(r2) <= le(r1) <= re(r1) <= re(r2)) and ((te(r2) >= te(r1) >= be(r2) >= be(r1)) or (te(r1) >= te(r2) >= be(r1) >= be(r2)))
#     isR1AcrossWidth = (le(r1) <= le(r2) <= re(r2) <= re(r1)) and ((te(r1) >= te(r2) >= be(r1) >= be(r2)) or (te(r2) >= te(r1) >= be(r2) >= be(r1)))
#     isR2AcrossHeight = (te(r2) >= te(r1) >= be(r1) >= be(r2)) and ((le(r2) <= le(r1) <= re(r2) <= re(r1)) or (le(r1) <= le(r2) <= re(r1) <= re(r2)))
#     isR1AcrossHeight = (te(r1) >= te(r2) >= be(r2) >= be(r1)) and ((le(r1) <= le(r2) <= re(r1) <= re(r2)) or (le(r2) <= le(r1) <= re(r2) <= re(r1)))
#
#     return isR1CompletelyInside or isR2CompletelyInside or isR2LeftIntersecting or isR2TopIntersecting or isR2RightIntersecting or isR2BottomIntersecting or isR2AcrossWidth or isR1AcrossWidth or isR2AcrossHeight or isR1AcrossHeight
#
#
def isNotIntersecting(r1, r2):
    r2OnRight = re(r1) < le(r2)
    r2OnLeft = re(r2) < le(r1)
    r2OnTop = be(r2) > te(r1)
    r2OnBottom = be(r1) > te(r2)
    return r2OnLeft or r2OnTop or r2OnRight or r2OnBottom

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if isNotIntersecting(r1,r2):
        return emptyRect()
    else:
        return getDefaultEdges(r1,r2)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    # print(intersect_rectangle(Rect(1, 11, 38, 93), Rect(78, 6, 33, 31)))  # exp -> [0, 0, -1, -1]
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
