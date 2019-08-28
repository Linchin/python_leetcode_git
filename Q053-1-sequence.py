"""
Q053 Maximum Subarray
Easy.

08/28/2019

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Follow up:

If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach,
which is more subtle.

Topic:
array
divide and conquer
dp

This version:
Kadane's algorithm
O(n)
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        begin = 0
        begin_temp = 0
        end = 0
        max_v = nums[0]

        nums_c = nums.copy()

        for i in range(1, len(nums_c)):

            if nums_c[i-1] >= 0:
                nums_c[i] += nums_c[i-1]
            else:
                begin_temp = i

            if nums_c[i] > max_v:
                begin = begin_temp
                end = i
                max_v = nums_c[i]

            print(begin, end)

        return nums[begin:end + 1]


a = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()
print(sol.maxSubArray(a))














