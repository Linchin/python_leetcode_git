"""
Q496
Next greater element
Easy

You are given two arrays (without duplicates) nums1 and
nums2 where nums1’s elements are subset of nums2. Find
all the next greater numbers for nums1's elements in
the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the
first greater number to its right in nums2. If it does
 not exist, output -1 for this number.
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []

        # use stack to generate the hashmap
        stack = [nums2[0]]
        hashmap = {}

        for i in range(1, len(nums2)):
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    hashmap[stack.pop()] = nums2[i]

                stack.append(nums2[i])

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap[_] for _ in nums1]

sol = Solution()

nums1 = [1, 2, 4]
nums2 = [1,2,3,4]

print(sol.nextGreaterElement(nums1, nums2))










