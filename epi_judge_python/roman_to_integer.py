from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    exceptionMap = {
        "I": ["V","X"],
        "X": ["L","C"],
        "C": ["D","M"],
        "L": [],
        "D": [],
        "M": [],
        "V": []
    }
    valueMap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    value = 0
    i = 0
    #dont need to worry about exceptions since we are getting a valid roman numeral input
    while i < len(s)-1:
        curr = s[i]
        next = s[i+1]
        if next in exceptionMap[curr]:
            value += valueMap[next] - valueMap[curr]
            i+=2
        else:
            value += valueMap[curr]
            i+=1
    if len(s) == 1 or s[-1] not in exceptionMap[s[-2]]:
        value += valueMap[s[-1]]
    return value


if __name__ == '__main__':
    # print(roman_to_integer("I"))
    # print(roman_to_integer("II"))
    # print(roman_to_integer("VI"))
    # print(roman_to_integer("IV"))
    # print(roman_to_integer("CXIX"))
    exit(generic_test.generic_test_main('roman_to_integer.py','roman_to_integer.tsv',roman_to_integer))
