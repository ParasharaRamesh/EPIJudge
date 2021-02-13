from test_framework import generic_test

def extractNumbersIntoList(x):
    l = []
    while x:
        l.append(x % 10)
        x//=10
    return l

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        numberList = extractNumbersIntoList(x)
        l = 0
        r = len(numberList) -1
        while l <=r:
            if numberList[l] == numberList[r]:
                l +=1
                r-=1
            else:
                return False
        return True

if __name__ == '__main__':
    # print(is_palindrome_number(123))
    # print(is_palindrome_number(12321))
    # print(is_palindrome_number(123321))
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
