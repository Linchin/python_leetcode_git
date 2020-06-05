"""
Q167
Two Sum II - input array is sorted
Easy

Array/TwoPointers/BinarySearch

Given an array of integers that is already sorted
in ascending order, find two numbers such that they
add up to a specific target number.

The function twoSum should return indices of the
two numbers such that they add up to the target,
where index1 must be less than index2.

Note:

- Your returned answers (both index1 and index2)
  are not zero-based.
- You may assume that each input would have exactly
  one solution and you may not use the same element
  twice.
"""

# 2018 solution

__author__ = 'linchin'
class Solution1:
    # brute force

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0,len(numbers)):

            comp = target - numbers[i]

            if comp in numbers[i+1:]:

                return [i+1, numbers[i+1:].index(comp)+1+i+1]



class Solution2:
    # from leetcode: double side sliding window
    # very fast


    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers)-1

        while numbers[i] + numbers[j] != target:

            if numbers[i] + numbers[j] > target:

                j -= 1

            else:

                i += 1

        return [i+1, j+1]

sol = Solution2()

print(sol.twoSum([2,7,11,15],9))

# 05/25/2020
# refresh

from typing import List

class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers)-1

        while numbers[lo] + numbers[hi] != target:
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            else:
                lo += 1

        return [lo+1, hi+1]

nums = [2, 7, 11, 15]
target = 9
sol2 = Solution3()
print(sol2.twoSum(nums, target))









