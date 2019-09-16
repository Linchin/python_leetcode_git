"""
Q560
Subarray Sum Equals K
Medium

Array; Hash Table.

Running sum;
O(n).

Given an array of integers and an integer k, you need to find the
total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range
of the integer k is [-1e7, 1e7].
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hash_table = defaultdict(lambda: 0)
        total = 0
        sum_r = sum_l = 0
        for item in nums:
            sum_r += item
            if sum_r - k in hash_table:
                total += hash_table[sum_r-k]
            if sum_r == k:
                total += 1
            hash_table[sum_r] += 1
            sum_l += item

        return total

nums = [1,0,1,0]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))








