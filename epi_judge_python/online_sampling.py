import functools
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
import random

#reservoir sampling !
# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    reservoir = []
    for i in range(k):
        x = next(stream)
        reservoir.append(x)
    #now your reservoir has at the minumum k elements
    curr = k+1
    while True:
        try:
            # randIndexToReplace = random.randrange(curr)
            x = next(stream)
            # if randIndexToReplace < k:
            if random.random() <= k/curr:
                #replace something from reservoir with this
                # reservoir[randIndexToReplace] = x
                reservoir[random.randrange(k)] = x
            curr+=1
        except Exception:
            break

    return reservoir


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda:
            [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    # for i in range(1000):
    #     i = iter(list(range(10)))
    #     print(online_random_sample(i, 1))
    exit(generic_test.generic_test_main('online_sampling.py','online_sampling.tsv',online_random_sample_wrapper))

