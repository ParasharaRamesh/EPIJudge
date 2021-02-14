from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    start = 0
    end = len(s) -1
    while start < end:
        startCh = s[start]
        endCh = s[end]
        if startCh.isalnum() and endCh.isalnum() and startCh.lower() == endCh.lower():
            start +=1
            end -=1
        elif not startCh.isalnum():
            start +=1
        elif not endCh.isalnum():
            end -=1
        else:
            return False

    return True


if __name__ == '__main__':
    # print(is_palindrome("a, man nama!."))
    exit(generic_test.generic_test_main('is_string_palindromic_punctuation.py','is_string_palindromic_punctuation.tsv', is_palindrome))
