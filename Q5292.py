"""
contest
12/21/2019
"""

from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if k == 1:
            return True

        if len(nums) % k:
            return False

        nums_dict = {}
        nums = sorted(nums, reverse=True)

        for number in nums:
            if number not in nums_dict:
                nums_dict[number] = 1
            else:
                nums_dict[number] += 1

        def remove_(v):
            nums_dict[v] -= 1
            if nums_dict[v] == 0:
                del nums_dict[v]

        while len(nums_dict) > 0:
            current = min(nums_dict.keys())
            remove_(current)

            for i in range(1, k):
                next = current + 1
                if next in nums_dict:
                    remove_(next)
                    current += 1
                else:
                    return False
        return True

sol = Solution()
nums = [3,2,1,2,3,4,3,4,5,9,10,12]
k = 3
print(sol.isPossibleDivide(nums, k))






