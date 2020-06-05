"""
Q001
Two Sum
Easy

Array/Hash table

Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly
one solution, and you may not use the same element twice.
"""


__author__ = 'linchin'



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Python2 Solution (from 2018)
# two sums
class Solution:
    def twoSum(self, l1, l2):

        dummy = sum = ListNode(0)

        carry = 0

        while l1 or l2 or carry:

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            sum.next = ListNode(carry%10)
            sum = sum.next

            carry //= 10

        return dummy.next



# Python 3 version
# 05/25/2020

from typing import List


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(0, len(nums)):
            if nums[i] not in hash:
                hash[target-nums[i]] = i
            else:
                return [hash[nums[i]], i]


sol = Solution2()
nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))





















