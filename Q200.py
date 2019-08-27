"""
Q200 Number of Islands
Medium
08/27/2019

Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

dfs. bfs, union find.

"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        visited = {}
        total = 0

        if n == 0:
            if grid[0] == '1':
                total += 1
            for i in range(1, m):
                if grid[i] == '1' and grid[i-1] != '1':
                    total += 1

        for i in range(0, m):
            for j in range(0, n):

                if grid[i][j] == '1' and (i,j) not in visited:

                    total += 1
                    visited[(i,j)] = 1

                    q = [(i,j)]

                    while q:

                        (ii, jj) = q.pop()

                        i_n = [ii, ii, ii+1, ii-1]
                        j_n = [jj+1, jj-1, jj, jj]

                        for item in zip(i_n, j_n):
                            if 0 <= item[0] < m and \
                                    0 <= item[1] < n and \
                                    grid[item[0]][item[1]] == '1':
                                if (item[0],item[1]) not in visited:
                                    visited[(item[0],item[1])] = 1
                                    q.append((item[0],item[1]))


        return total


sol = Solution()

a = ["1","0","1","0","1"]

print(sol.numIslands(a))




