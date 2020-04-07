"""
Q064
Minimum path sum
Medium

Dynamic Programming


Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point
in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def dp(x, y):

            if x == 0 and y == 0:
                return grid[x][y]
            elif x == 0:
                return grid[x][y] + grid[0][y-1]
            elif y == 0:
                return grid[x][y] + grid[x-1][0]
            else:
                return grid[x][y] + min(grid[x-1][y], grid[x][y-1])


        for x in range(m):
            for y in range(n):
                grid[x][y] = dp(x, y)


        return grid[-1][-1]


sol = Solution()
mat = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(sol.minPathSum(mat))









