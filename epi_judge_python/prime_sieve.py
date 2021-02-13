from typing import List
from math import fabs, inf
import copy
from test_framework import generic_test


def markNonPrimes(currPrime, primalityList):
    low = 2
    i = 2
    while i*currPrime <= len(primalityList) + 1:
        if primalityList[i*currPrime - low]:
            primalityList[i*currPrime - low] = False
        i+=1
    return primalityList


def getNextPrimeContender(primalityList, primes):
    # bool list from [2, n]

    low = 2
    for i, primality in enumerate(primalityList):
        if primality and i + low not in primes:
            return i + low

    return low + len(primalityList)


def addIfPrime(n, primes):
    for prime in primes:
        if n % prime == 0:
            return primes

    primes.append(n)
    return primes

# Given n, return all primes up to and including n.
cache = {}


def getClosestPrimesAndPrimalityListFromCache(n):
    #  return list of primes of the closest n and also its primality list after performing all the marking
    #first get the nearestN greater than (if present or less than)
    diff = inf
    nearestN = -1
    for k in sorted(cache.keys()):
        if k > n:
            nearestN = k
            break
    if nearestN == -1:
        nearestN = sorted(cache.keys())[-1]

    #get it the stuff from the cache
    return k, copy.deepcopy(cache[nearestN][0]), copy.deepcopy(cache[nearestN][1])

def addToCache(n, primes, primalityList):
    if n not in cache:
        cache[n] = [primes, primalityList]

def initCache():
    cache[2] = [[2], [True]]

def generate_primes(n: int) -> List[int]:
    if n < 2:
        return []

    if len(cache.keys()) == 0:
        initCache()

    nearestNumInCache, primes , primalityList = getClosestPrimesAndPrimalityListFromCache(n)

    # primes = [2]
    # primalityList = [True for i in range(2, n + 1)]
    if len(primalityList) < n:
        #add more True's
        diff = n - 1 - len(primalityList)
        primalityList.extend([True] * diff)
        for prime in primes:
            primalityList = markNonPrimes(prime, primalityList)

    if nearestNumInCache < n:
        while True:
            # pick the last element in primes
            # mark every multiple as false
            primalityList = markNonPrimes(primes[-1], primalityList)

            # find the nearest isNumberPrime number and check with existing primes and then add to primes
            primeContender = getNextPrimeContender(primalityList, primes)
            if primeContender <= n:
                primes = addIfPrime(primeContender, primes)
            else:
                break
    else:
        primes = list(filter(lambda prime: prime <= n, primes))
    addToCache(n, primes, primalityList)
    return primes


if __name__ == '__main__':
    print(generate_primes(20))
    print(generate_primes(100))
    print(generate_primes(200))
    print(generate_primes(50))
    print(generate_primes(500))
    print(generate_primes(1000))
    print(generate_primes(4000))

    exit(generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',generate_primes))
