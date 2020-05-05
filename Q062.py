"""
Q062
Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        distance = [[1] * m for ii in range(n)]

        def find(i, j):
            if i == 0 or j == 0:
                return
            else:
                distance[j][i] = distance[j-1][i] + distance[j][i-1]

        for i in range(m):
            for j in range(n):
                find(i, j)

        return distance[-1][-1]


sol = Solution()

print(sol.uniquePaths(7, 3))



