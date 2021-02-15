from test_framework import generic_test

def say_next(prev_say):
    next_say = ""
    i = 0
    while i < len(prev_say)-1:
        #count forward until next diff element appears
        curr = prev_say[i]
        j = i+1
        while j < len(prev_say) and prev_say[j] == curr:
            j+=1
        count = j - i
        next_say += f"{count}{curr}"
        i = j

    #worry about last character being unique
    if len(next_say) == 0 or prev_say[-1] != next_say[-1]:
        next_say += f"1{prev_say[-1]}"

    return next_say

def look_and_say(n: int) -> str:
    i = 2
    currSay = "1"
    while i <= n:
        currSay = say_next(currSay)
        i+=1
    return currSay


if __name__ == '__main__':
    # print(say_next("1"))
    # print(say_next("12"))
    # print(say_next("11"))
    # print(say_next("11122"))
    # print(say_next("111223333"))
    # print(say_next("111223333444"))
    # print(look_and_say(1))
    # print(look_and_say(2))
    # print(look_and_say(3))
    # print(look_and_say(8))
    exit(generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',look_and_say))
