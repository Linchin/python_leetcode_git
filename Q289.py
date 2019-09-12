"""
Q289
Game of Life
Medium

/array/

According to the Wikipedia's article: "The Game of Life,
also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial
state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia
article):

* Any live cell with fewer than two live neighbors
dies, as if caused by under-population.
* Any live cell with two or three live neighbors lives
on to the next generation.
* Any live cell with more than three live neighbors dies,
as if by over-population..
* Any dead cell with exactly three live neighbors becomes
a live cell, as if by reproduction.

Write a function to compute the next state (after one
update) of the board given its current state. The next
state is created by applying the above rules simultaneously
to every cell in the current state, where births and deaths
occur simultaneously.

Example:
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:
1. Could you solve it in-place? Remember that the board needs to be
updated at the same time: You cannot update some cells first and
then use their updated values to update other cells.

2. In this question, we represent the board using a 2D array. In
principle, the board is infinite, which would cause problems when
the active area encroaches the border of the array. How would you
address these problems?
"""

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                count = 0
                if i - 1 >= 0 and j - 1 >= 0: count += board[i-1][j-1]%2
                if i - 1 >= 0: count += board[i-1][j]%2
                if i - 1 >= 0 and j + 1 <= n - 1: count += board[i-1][j+1]%2
                if j - 1 >= 0: count += board[i][j-1]%2
                if j + 1 <= n - 1: count += board[i][j+1]%2
                if i + 1 <= m - 1 and j - 1 >= 0: count += board[i+1][j-1]%2
                if i + 1 <= m - 1: count += board[i+1][j]%2
                if i + 1 <= m - 1 and j + 1 <= n - 1: count += board[i+1][j+1]%2

                if board[i][j] == 1:
                    if count == 2 or count == 3:
                        board[i][j] += 2
                        continue

                else:
                    if count == 3:
                        board[i][j] += 2

        for i in range(0, m):
            for j in range(0, n):
                board[i][j] //= 2


a = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

sol = Solution()
sol.gameOfLife(a)
print(a)

