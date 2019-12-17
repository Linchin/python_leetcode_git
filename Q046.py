"""
Q046
permutations
Medium

Backtracking.

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def tracking(perm, nums):
            if not nums:
                perms.append(perm)
                return
            for item in nums:
                nums_new = nums.copy()
                nums_new.remove(item)
                tracking(perm+[item], nums_new)

        perms = []

        tracking([], nums)

        return perms



sol = Solution()
a = [1,2,3]
print(sol.permute(a))





