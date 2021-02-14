import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import deque

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
#word ending indices [12,5,2]
def reverse_words(s):
    copyS = s[:]
    no_of_words = 1
    word_ending_indices = deque()

    for i,ch in enumerate(s):
        if ch == " ":
            no_of_words +=1
            word_ending_indices.appendleft(i-1)

    word_ending_indices.appendleft(len(s)-1)
    if no_of_words == 1:
        return s


    firstWordEnd = word_ending_indices[-1]

    #take last word and insert in beginning
    currWordEnd = 0
    for i in range(len(word_ending_indices)-1):
        firstWordEnd += word_ending_indices[i] - word_ending_indices[i+1]
        toInsert = copyS[word_ending_indices[i+1] + 2: word_ending_indices[i] + 1] + [" "]
        for j,ch in enumerate(toInsert):
            s.insert(currWordEnd + j,ch)
        currWordEnd += len(toInsert)

    #delete everything past the last index
    for i in range(firstWordEnd + 1, len(s)):
        s.pop(firstWordEnd +1)

    return s



@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    # print(reverse_words(['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']))
    # print(reverse_words(['r', 'a', 'm', ' ', 'i', 's']))
    # print(reverse_words(['r', 'a', 'm']))
    exit(generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',reverse_words_wrapper))
