"""
contest
"""
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for number in nums:

            if not number:
                continue

            digits = 0
            while number:
                digits += 1
                number = number // 10
            if digits % 2 == 0:
                count += 1
        return count

sol = Solution()
a = [555,901,482,1771]
print(sol.findNumbers(a))
