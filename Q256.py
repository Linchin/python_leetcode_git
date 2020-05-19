"""
Q256
Paint House
Easy

:Dynamic Programming:

There are a row of n houses, each house can be painted with one
of the three colors: red, blue or green. The cost of painting
each house with a certain color is different. You have to paint
all the houses such that no two adjacent houses have the same
color.

The cost of painting each house with a certain color is represented
by a n x 3 cost matrix. For example, costs[0][0] is the cost of
painting house 0 with color red; costs[1][2] is the cost of painting
house 1 with color green, and so on... Find the minimum cost to paint
all houses.

Note:
All costs are positive integers.

"""

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        if len(costs) == 0:
            return 0

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])


cost = [[17,2,17],[16,16,5],[14,3,19]]
sol = Solution()
print(sol.minCost(cost))

