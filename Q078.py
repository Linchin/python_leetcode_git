"""
Q078
Subsets
Medium

Backtracking.

Given a set of distinct integers, nums, return all
possible subsets (the power set).

Note: The solution set must not contain duplicate
subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        total = len(nums)

        power_set = []

        for i in range(0, 2 ** total):

            format_s = "0" * total + "b"
            string = format(i, "b").zfill(total)
            new_set = []
            for j in range(0, total):
                new_set += [nums[j]] * int(string[j])

            power_set.append(new_set)


        return power_set

sol = Solution()

nums = [1, 2, 3]

print(sol.subsets(nums))












