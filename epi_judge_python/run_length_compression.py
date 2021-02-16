from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    dec = ""
    i = 0
    while i < len(s):
        num = s[i]
        j = i+1
        while j < len(s) and s[j].isnumeric():
            num += s[j]
            j+=1
        char = s[j]
        dec += char*int(num)
        i = j+1
    return dec

def encoding(s: str) -> str:
    enc = ""
    i = 0
    while i < len(s):
        curr = s[i]
        count = 1
        j = i+1
        while j < len(s) and s[j] == curr:
            count +=1
            j+=1
        enc += f"{count}{curr}"
        i+=count

    return enc


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    # s = "10q13a8b2m17c"
    # d = decoding(s)
    # e = encoding(d)
    # print(d)
    # print(e)
    # print(s == e)
    exit(generic_test.generic_test_main('run_length_compression.py','run_length_compression.tsv',rle_tester))
