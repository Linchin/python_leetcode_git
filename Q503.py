"""
Q503
Next Greater Element II
Medium

Given a circular array (the next element of the last element
is the first element of the array), print the Next Greater
Number for every element. The Next Greater Number of a
number x is the first greater number to its traversing-order
next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist,
output -1 for this number.

"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:


        if not nums:
            return []

        stack = [0]
        next_great = [-1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] <= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    next_great[stack.pop()] = nums[i]
                stack.append(i)

        for i in range(0, len(nums)):

            if nums[i] <= nums[stack[-1]] and next_great[i] == -1:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    next_great[stack.pop()] = nums[i]
                stack.append(i)

        return next_great


sol = Solution()
input = [1,2,3,2,1]
print(sol.nextGreaterElements(input))


















