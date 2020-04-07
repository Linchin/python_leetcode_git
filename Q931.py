"""
Q931
Minimum Falling Path Sum
Medium

Given a square array of integers A, we want the minimum sum
of a falling path through A.

A falling path starts at any element in the first row, and
chooses one element from each row.  The next row's choice
must be in a column that is different from the previous
row's column by at most one.


"""

from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        m = len(A)

        def dp(x, y):
            if y == 0:
                A[x][y] += min(A[x-1][0], A[x-1][1])
            elif y == m-1:
                A[x][y] += min(A[x-1][m-1], A[x-1][m-2])
            else:
                A[x][y] += min(A[x-1][y-1], A[x-1][y], A[x-1][y+1])

        for x in range(1, m):
            for y in range(0, m):
                dp(x, y)

        return min(A[-1])


sol = Solution()
A = [[1,1,1],[5,3,1],[2,3,4]]

print(sol.minFallingPathSum(A))









