"""
Q169
Majority Element
Easy

Array topic

Given an array of size n, find the majority element. The majority
element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority
element always exist in the array.
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        length = len(nums)
        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1
            if count[item]/length >= 1/2:
                return item


sol = Solution()
input = [2,3,3]
print(sol.majorityElement(input))

















