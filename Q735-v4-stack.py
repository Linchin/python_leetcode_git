"""
Q735
Asteroid Collision
Medium

v4
using stack, which is from the solution.

11.19.2019 revision
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

        final = []
        for item in asteroids:
            while final and item < 0 < final[-1]:
                if final[-1] < -item:
                    final.pop()
                    continue
                elif final[-1] == -item:
                    final.pop()
                    break
                else:
                    break
            else:
                final.append(item)

        return final



sol = Solution()
a = asteroids = [10, 2, -5]
print(sol.asteroidCollision(a))

