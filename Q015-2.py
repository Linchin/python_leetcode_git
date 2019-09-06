"""
Q015
3Sum
Medium

20190906

Try to check duplication automatically.

/Array
Two pointers/

Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        a = []

        sort_n = sorted(nums)

        N = len(sort_n)

        last = None

        for i in range(0, N-2):

            if sort_n[i] == last:
                continue

            last = sort_n[i]
            temp_j = None
            temp_n = None

            j = i + 1
            n = N-1

            while j < n:

                if sort_n[i] + sort_n[j] + sort_n[n] > 0:
                    temp = sort_n[n]
                    while sort_n[n] == temp and j < n:
                        n -= 1
                    continue

                if sort_n[i] + sort_n[j] + sort_n[n] < 0:
                    temp = sort_n[j]
                    while sort_n[j] == temp and j < n:
                        j += 1
                    continue

                if sort_n[i] + sort_n[j] + sort_n[n] == 0:
                    a.append([sort_n[i], sort_n[j], sort_n[n]])
                    temp_j = sort_n[j]
                    temp_n = sort_n[n]
                    while sort_n[j] == temp_j:
                        j += 1
                    while sort_n[n] == temp_n:
                        n -= 1
                    continue

        return a

k = [1,-1,-1,0]
sol = Solution()
print(sol.threeSum(k))





