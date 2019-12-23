"""
Q042
Trapping Rain Water
Hard

:stack:two pointer:array: DP:

Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it
is able to trap after raining.

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if not height or len(height) < 3:
            return 0

        water = 0
        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = left[1] = height[0]
        right[-1] = right[-2] = height[-1]

        for i in range(2, len(height)):
            if height[i-1] > left[i-1]:
                left[i] = height[i-1]
            else:
                left[i] = left[i-1]
            if height[len(height)-i] > right[len(height)-i]:
                right[len(height)-i-1] = height[len(height)-i]
            else:
                right[len(height)-i-1] = right[len(height)-i]

        for i in range(1, len(height)-1):
            water += max(0, min(left[i], right[i]) - height[i])

        return water

a =  [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(a))




