"""
Q016
3Sum Closest
Medium

Array

Given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target. Return the
sum of the three integers. You may assume that each input would
have exactly one solution.

"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        total = len(nums)

        if total == 3:
            return sum(nums)

        nums = sorted(nums)

        closest = float('inf')

        for l in range(0, total-2):
            for r in range(l+2, total):
                m_min = l + 1
                m_max = r - 1
                while 1:
                    if m_min == m_max:
                        current_total = nums[l] + nums[m_min] + nums[r]
                        if abs(current_total-target) < abs(closest-target):
                            closest = current_total
                        break
                    elif m_min + 1 == m_max:
                        for m in (m_min, m_max):
                            current_total = nums[l] + nums[m] + nums[r]
                            if abs(current_total - target) < abs(closest - target):
                                closest = current_total
                        break
                    else:
                        m = int((m_min + m_max) / 2)
                        current_total = nums[l] + nums[m] + nums[r]
                        if current_total == target:
                            return target
                        elif current_total > target:
                            m_max = m
                        else:
                            m_min = m

        return closest

sol = Solution()
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2

print(sol.threeSumClosest(nums, target))

