from typing import List
from test_framework import generic_test

def computeMonotonicity(l):
    montonicity = [None] * (len(l))
    if len(l) >= 2:
        montonicity[-2] = l[-2] <= l[-1]
        i = len(l) - 3
        while i >=0:
            curr = l[i]
            next = l[i+1]
            if curr <= next:
                if montonicity[i+1]:
                    montonicity[i] = True
                else:
                    montonicity[i] = None
            else:
                if montonicity[i+1] or montonicity[i+1] == None:
                    montonicity[i] = None
                elif not montonicity[i+1]:
                    montonicity[i] = False
            i -=1
    return montonicity

def isIncreasingSequence(i, l):
    return l[i]
    # #true, false, None
    # if len(l) == 1:
    #     return None
    # elif len(l) == 2:
    #     return l[1] >= l[0]
    # else:
    #     isIncreasing = l[1] >= l[0]
    #     i = 2
    #     while i < len(l):
    #         if l[i-1] <= l[i]:
    #             if not isIncreasing:
    #                 return None
    #         elif isIncreasing:
    #             return None
    #         i+=1
    #     return isIncreasing
    
def buy_and_sell_stock_once(prices: List[float]) -> float:
    monotonicity = computeMonotonicity(prices)
    # TODO - you fill in here.
    best = 0.0
    pricesLen = len(prices)
    
    for i in range(pricesLen - 1):
        maxDifference = 0.0
        isIncreasing = isIncreasingSequence(i+1,monotonicity)
        l = i + 1
        r = pricesLen - 1

        if isIncreasing == None:
            #find max using O(n/2)
            while l <= r:
                leftEle = prices[l]
                rightEle = prices[r]
                currEle = prices[i]
                betterDiffBtnLAndR = max(leftEle,rightEle) - currEle
                if betterDiffBtnLAndR > maxDifference:
                    maxDifference = betterDiffBtnLAndR
                    betterDiffBtnLAndR = 0
                l += 1
                r -= 1
        elif isIncreasing:
            return max(best, prices[r] - min(prices[l],prices[i]))
        else:
            return max(best, prices[l] - prices[i])
        best = max(best, maxDifference)

    return best


if __name__ == '__main__':
    # print(computeMonotonicity([310,315,275,295,260,270,290,230,255,250]))
    # print(computeMonotonicity([310]))
    # print(computeMonotonicity([]))
    # print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
