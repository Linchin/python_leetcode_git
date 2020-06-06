"""
Q442
Find all duplicates in an array
medium

Given an array of integers, 1 ≤ a[i] ≤ n
(n = size of array), some elements appear
twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        dup = []

        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                dup.append(abs(nums[i]))

        return dup

sol = Solution()
nums = [2,2]
print(sol.findDuplicates(nums))

