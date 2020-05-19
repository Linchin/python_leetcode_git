"""
Q714
Best time to buy and sell stocks with transaction fee
Medium

DP

Your are given an array of integers prices, for
which the i-th element is the price of a given
stock on day i; and a non-negative integer fee
representing a transaction fee.

You may complete as many transactions as you
like, but you need to pay the transaction fee
for each transaction. You may not buy more than
1 share of a stock at a time (ie. you must sell
the stock share before you buy again.)

Return the maximum profit you can make.

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)

        if n == 0:
            return 0

        # hold after ith time
        hold = [0] * n
        hold[0] = -prices[0]

        # empty after ith time
        empty = [0] * n

        for i in range(1, n-1):
            hold[i] = max(hold[i-1], empty[i-1]-prices[i])
            empty[i] = max(hold[i-1]+prices[i]-fee, empty[i-1])


        return max(hold[n-2]+prices[n-1]-fee, empty[n-2])


sol = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2

print(sol.maxProfit(prices, fee))







