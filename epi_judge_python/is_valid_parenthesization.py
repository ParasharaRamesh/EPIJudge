from test_framework import generic_test

def getCorrespondingOpeningBracket(b):
    brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    return brackets[b] if b in brackets else None

def is_well_formed(s: str) -> bool:
    bracketStack = []
    for ch in s:
        if len(bracketStack) == 0:
            bracketStack.append(ch)
        else:
            corr = getCorrespondingOpeningBracket(ch)
            top = bracketStack[-1]
            if corr == None:
                #means its an opening bracket
                bracketStack.append(ch)
            elif corr == top:
                bracketStack.pop()
            else:
                return False
    return len(bracketStack) == 0


if __name__ == '__main__':
    # print(is_well_formed("(){)}"))
    exit(generic_test.generic_test_main('is_valid_parenthesization.py','is_valid_parenthesization.tsv',is_well_formed))
