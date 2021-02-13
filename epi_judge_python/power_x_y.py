from test_framework import generic_test
from functools import lru_cache

cache = dict()

def memoise(func):
    def wrapper(x,y):
        return cache.setdefault((x,y), func(x,y))
    return wrapper


# def power(x: float, y: int) -> float:
#     if y==0:
#         return 1
#     if y ==1:
#         return x
#     if y == -1:
#         return 1/x
#     sqrt = power(x, y//2)
#     ans = sqrt*sqrt
#     return ans * x if y %2 ==1 else ans

@memoise
def power(x: float, y: int) -> float:
    global cache
    if y==0:
        return 1
    if y ==1:
        return x
    if y == -1:
        return 1/x
    sqrt = power(x, y//2)
    ans = sqrt*sqrt
    return ans * x if y %2 ==1 else ans



if __name__ == '__main__':
    # print(memoise(power)(12,5))
    # print(power(12,5))
    generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv', power)
    exit(print(cache))

