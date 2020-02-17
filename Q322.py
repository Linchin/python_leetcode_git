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

"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        min_dict = {0: 0}
        for item in coins:
            min_dict[item] = 1

        min_coin = min(coins)

        coins_sorted = sorted(coins)
        steps = [coins_sorted[i+1] - coins_sorted[i] for i in range(len(coins_sorted)-1)]

        min_step = min(steps+coins_sorted)

        def find_min(num):
            sum_ = num+1

            if num in min_dict:
                return

            i = min_coin
            while i <= (num+1)//2+2:
                if i in min_dict and num-i in min_dict:
                    sum_ = min(sum_, min_dict[i]+min_dict[num-i])
                    i += min_step
                else:
                    i += 1


#            for i in range(min_coin, (num+1)//2+2):
#                if i in min_dict and num-i in min_dict:
#                    sum_ = min(sum_, min_dict[i]+min_dict[num-i])

            if sum_ == num+1:
                return None
            else:
                min_dict[num] = sum_
                return True

        i = 0
        while i <= amount:
            if find_min(i) is None:
                i += 1
            else:
                i += min_step


    #    for i in range(0, amount+1):
    #        find_min(i)

        if amount not in min_dict:
            return -1
        else:
            return min_dict[amount]


sol = Solution()
coins = [431, 62, 88, 428]
amount = 9084
print(sol.coinChange(coins, amount))






