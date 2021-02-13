from test_framework import generic_test


def parity_bruteforce(x: int) -> int:
    # 1 if everything is odd, else 0
    count = 0
    while x: 
        if x & 1:
            count +=1
        x >>= 1

    return 0 if count%2 == 0 else 1

def parity(x: int) -> int:
    # 1 if everything is odd, else 0
    count = 0
    while x: 
        x =  x & (x-1)
        count+=1

    return 0 if count%2 == 0 else 1


if __name__ == '__main__':
    # print(parity(4))
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
