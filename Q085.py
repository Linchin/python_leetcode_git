"""
Q085
Maximal Rectangle
Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest
rectangle containing only 1's and return its area.
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        left_bound = 0
        right_bound = n

        max_area = 0

        for i in range(m):

            left_bound = 0
            right_bound = n

            for j in range(n):

                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], left_bound)
                else:
                    height[j] = 0
                    left[j] = 0
                    left_bound = j+1

            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], right_bound)
                else:
                    right[j] = n
                    right_bound = j

            for j in range(0, n):
                max_area = max(max_area,
                               height[j]*(right[j]-left[j]))

        return max_area

sol = Solution()

mat = [["1"]]

print(sol.maximalRectangle(mat))




