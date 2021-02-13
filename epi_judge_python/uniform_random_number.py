import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)

def no_of_bits_of_nearest_higher_power_of_2(x):
    return int(math.ceil(math.log2(x)))

def generate_binary_no(num_bits):
    res = 0
    for i in range(num_bits):
        ithbit = zero_one_random()
        res |= ithbit << i
    return res

def uniform_random(lower_bound: int, upper_bound: int) -> int:
    r = upper_bound - lower_bound + 1
    n = no_of_bits_of_nearest_higher_power_of_2(r)
    pick = 0
    # call the random method that many times and based off the binary you get return that - let that binary number be pick
    while True:
        pick = generate_binary_no(n)
        if pick >= r:
            pick = generate_binary_no(n)
        else:
            break
    return lower_bound + pick


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    # while True:
    #     print(uniform_random(3,7))
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
