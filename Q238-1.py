"""
Q238
Product of Array Except Self
Medium

/Array/
O(n) time complexity
O(n) space complexity

Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does
 not count as extra space for the purpose of space complexity analysis.)

"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return 0

        left = [1] * len(nums)
        right = [1] * len(nums)

        prod = [1] * len(nums)

        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i]

        for i in reversed(range(0, len(nums)-1)):
            right[i] = right[i+1] * nums[i]

        for i in range(1, len(nums)-1):
            prod[i] = left[i-1] * right[i+1]

        prod[0] = right[1]
        prod[-1] = left[-2]

        return prod

sol = Solution()
a = [1,2]
print(sol.productExceptSelf(a))























