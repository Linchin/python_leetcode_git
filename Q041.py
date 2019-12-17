"""
Q041
First Missing Positive
Hard

array;

Given an unsorted integer array, find the smallest missing
positive integer.

Note:
Your algorithm should run in O(n) time and uses constant
extra space.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        L = len(nums)
        max_val = max(nums)

        if max_val < 1:
            return 1

        for i in range(L):
            if nums[i] <= 0:
                nums[i] = max_val

        min_val = min(nums)

        if min_val > 1:
            return 1

        missing = 2
        while True:

            flag = False
            for item in nums:
                if item == missing:
                    flag = True

            if flag:
                missing += 1
                if missing > max_val:
                    return missing
                continue
            else:
                return missing



sol = Solution()
a = [1,2,0]
print(sol.firstMissingPositive(a))


