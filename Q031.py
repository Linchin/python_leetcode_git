"""
Q031 Next Permutation
Medium

Array;

Implement next permutation, which rearranges numbers
into the lexicographically next greater permutation of numbers.
(that means the order in dictionary)

If such arrangement is not possible, it must rearrange it
as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra
memory.

Here are some examples. Inputs are in the left-hand column
and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        total = len(nums)

        for i in reversed(range(1, total)):

            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                break

            for j in range(i, total):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

            for j in range(i, total):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]


a = [2, 3, 1]

sol = Solution()
sol.nextPermutation(a)
print(a)