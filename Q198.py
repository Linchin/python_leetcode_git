"""
Q198
House Robber
Easy

:Dynamic Programming:

You are a professional robber planning to rob houses along a
street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the
amount of money of each house, determine the maximum
amount of money you can rob tonight without alerting the
 police.

Analysis:
You either skip one or skip two.
For each node, we either have skip one skip two or adjacent.
That is, if we use this node, then we consider the bigger
value between skip one and skip two.

Then we save the value of not using this node - also
skip one or skip two.

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        sum_0 = 0
        sum_1 = 0

        for num in nums:
            temp = sum_0
            sum_0 = max(sum_0, sum_1)
            sum_1 = temp + num

        return max(sum_0, sum_1)


sol = Solution()
a = [2,7,9,3,1]
print(sol.rob(a))



