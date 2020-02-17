"""
Q322
Coin Change
Medium


Dynamic Programming

You are given coins of different denominations and a total
amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination
of the coins, return -1.


Bottom Up method
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        min_dict = {0: 0}

        for i in range(amount + 1):
            min_num = float('inf')
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    if i-coin in min_dict:
                        min_num = min(min_num, min_dict[i-coin]+1)
            if min_num != float('inf'):
                min_dict[i] = min_num

        if amount not in min_dict:
            return -1
        else:
            return min_dict[amount]


sol = Solution()
coins = [431, 62, 88, 428]
amount = 9084
print(sol.coinChange(coins, amount))






