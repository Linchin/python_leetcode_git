"""
Q746
Min Cost Climbing Stairs
Easy

On a staircase, the i-th step has some non-negative
cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two
steps. You need to find minimum cost to reach the top
of the floor, and you can either start from the step
with index 0, or the step with index 1.

* cost will have a length in the range [2, 1000].
* Every cost[i] will be an integer in the range [0, 999].
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost:
            return 0

        costs = [[0] * len(cost), [0] * len(cost)]

        costs[1][0] = cost[0]

        for i in range(1, len(cost)):
            costs[0][i] = costs[1][i-1]
            costs[1][i] = min(costs[1][i-1], costs[0][i-1]) + cost[i]

        return min(costs[0][-1], costs[1][-1])


cost = [10, 15, 20]
sol = Solution()
print(sol.minCostClimbingStairs(cost))




