"""
Q1155
NUmber of dice rolls with target sum
medium

You have d dice, and each die has f faces numbered
1, 2, ..., f.

Return the number of possible ways (out of fd total
ways) modulo 10^9 + 7 to roll the dice so the sum of
the face up numbers equals target.

"""
from functools import lru_cache

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        if target < d:
            return 0

        @lru_cache(maxsize=None)
        def find(num, t):

            if num == 1:
                if 1 <= t <= f:
                    return 1
                else:
                    return 0

            if t < 0:
                return 0

            total = 0

            for i in range(1, f+1):
                total += find(num-1, t-i)

            #print(num, t, total)
            return total

        return find(d, target) % (10**9+7)

sol = Solution()
print(sol.numRollsToTarget(30, 30, 500))

