"""
Q048
Rotate image
Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means
you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(0, int((n)/2)):
            for j in range(0, int((n+1)/2)):
                temp = matrix[i][j]
                matrix[j][n-1-i], temp = temp, matrix[j][n-1-i]
                matrix[n-1-i][n-1-j], temp = temp, matrix[n-1-i][n-1-j]
                matrix[n-1-j][i], temp = temp, matrix[n-1-j][i]
                matrix[i][j] = temp


sol = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

sol.rotate(matrix)
print(matrix)







