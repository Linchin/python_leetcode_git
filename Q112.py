"""
Q112
Best Time to Buy and Sell Stock II
Easy

:greedy:
:array:

Say you have an array for which the ith element is the
price of a given stock on day i.

Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (i.e., buy one
and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the
same time (i.e., you must sell the stock before you buy
again).

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]

        return profit


