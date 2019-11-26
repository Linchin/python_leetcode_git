"""
Q605
Can Place Flowers
Easy

Array.

Suppose you have a long flowerbed in which some of the plots
are planted and some are not. However, flowers cannot be planted
in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1,
where 0 means empty and 1 means not empty), and a number n, return
if n new flowers can be planted in it without violating the
no-adjacent-flowers rule.

Note:
1. The input array won't violate no-adjacent-flowers rule.
2. The input array size is in the range of [1, 20000].
3. n is a non-negative integer which won't exceed the input array size.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        if len(flowerbed) == 1:
            if sum(flowerbed) + n == 1:
                return True
            else:
                return False

        count = n
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[0] == flowerbed[1] == 0:
                    count -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[-1] == flowerbed[-2] == 0:
                    count -= 1
            else:
                if flowerbed[i-1] == flowerbed[i+1] == flowerbed[i] == 0:
                    count -= 1
                    flowerbed[i] = 1
            if count == 0:
                return True

        return False

sol = Solution()
flowerbed = [1,0,0,0,1]
n = 2
print(sol.canPlaceFlowers(flowerbed, n))
