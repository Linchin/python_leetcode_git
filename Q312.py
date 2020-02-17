"""
Q312
Burst Balloons
Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted
with a number on it represented by array nums. You are asked to
burst all the balloons. If the you burst balloon i you will get
nums[left] * nums[i] * nums[right] coins. Here left and right are
adjacent indices of i. After the burst, the left and right then
becomes adjacent.

Find the maximum coins you can collect by bursting the balloons
wisely.

Note:

- You may imagine nums[-1] = nums[n] = 1. They are not real
  therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Top down;

"""


from typing import List
from functools import lru_cache


class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
        # If maxsize is set to None, the LRU feature is
        # disabled and the cache can grow without bound.

            if left + 1 == right:
                return 0

            return max(dp(left, i) + nums[left]*nums[i]*nums[right] + dp(i, right)
                       for i in range(left+1, right))

        return dp(0, len(nums)-1)


a = [3, 1, 5, 8]
sol = Solution()
print(sol.maxCoins(a))



