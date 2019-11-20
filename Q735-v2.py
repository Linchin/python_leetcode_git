"""
Q735
Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a
row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids
meet, the smaller one will explode. If both are the same size, both will
explode. Two asteroids moving in the same direction will never meet.

Note:
* The length of asteroids will be at most 10000.
* Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if not asteroids:
            return []

        count = 1
        temp = asteroids.copy()

        while count:
            count = 0
            next_iter = [temp[0]]
            for i in range(1, len(temp)):
                if next_iter[-1] > 0 and temp[i] < 0:
                    if abs(next_iter[-1]) < abs(temp[i]):
                        next_iter[-1] = temp[i]
                        count += 1
                else:
                    next_iter.append(temp[i])
            temp = next_iter.copy()

        return temp

sol = Solution()
a = asteroids = [-2,1,-1,-1]
print(sol.asteroidCollision(a))

