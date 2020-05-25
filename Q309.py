"""
Q309
Best Time to Buy and Sell Stock with Cooldown
Medium


Say you have an array for which the ith element is the
price of a given stock on day i.

Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (ie, buy one and
sell one share of the stock multiple times) with the
following restrictions:

You may not engage in multiple transactions at the same
time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next
day. (ie, cooldown 1 day)


"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        if n == 0:
            return 0

        # hold after the ith time
        hold = [0] * n
        hold[0] = -prices[0]

        # empty after the ith time
        empty = [0] * n

        for i in range(1, n-1):
            hold[i] = max(hold[i-1], empty[i-2]-prices[i])
            empty[i] = max(empty[i-1], hold[i-1]+prices[i])

        return max(empty[n-2], hold[n-2]+prices[n-1])



sol = Solution()
prices = [1,2,3,0,2]
print(sol.maxProfit(prices))


