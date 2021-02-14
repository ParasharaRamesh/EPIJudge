import string

from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    col = col.upper()
    charToValueMap = {chr(ord("A") + i - 1): i for i in range(1, 27)}
    res = 0
    for i , ch in enumerate(reversed(col)):
        res += (26 ** i) *  charToValueMap[ch]
    return res



if __name__ == '__main__':
    # print(ss_decode_col_id("D"))
    # print(ss_decode_col_id("ZZ"))
    # print(ss_decode_col_id("AA"))
    exit(generic_test.generic_test_main('spreadsheet_encoding.py','spreadsheet_encoding.tsv',ss_decode_col_id))
