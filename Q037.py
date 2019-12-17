"""
Q037
Sodoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty
cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of
    the 9 3x3 sub-boxes of the grid.
4. Empty cells are indicated by the character '.'.


Note:
1. The given board contain only digits 1-9 and the character '.'.
2. You may assume that the given Sudoku puzzle will have a single
    unique solution.
3. The given board size is always 9x9.
"""

from typing import List
import copy


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        panels = {(0, 0): [(0, 0), (0, 1), (0, 2),
                           (1, 0), (1, 1), (1, 2),
                           (2, 0), (2, 1), (2, 2)],
                  (0, 1): [(0, 3), (0, 4), (0, 5),
                           (1, 3), (1, 4), (1, 5),
                           (2, 3), (2, 4), (2, 5)],
                  (0, 2): [(0, 6), (0, 7), (0, 8),
                           (1, 6), (1, 7), (1, 8),
                           (2, 6), (2, 7), (2, 8)],
                  (1, 0): [(3, 0), (3, 1), (3, 2),
                           (4, 0), (4, 1), (4, 2),
                           (5, 0), (5, 1), (5, 2)],
                  (1, 1): [(3, 3), (3, 4), (3, 5),
                           (4, 3), (4, 4), (4, 5),
                           (5, 3), (5, 4), (5, 5)],
                  (1, 2): [(3, 6), (3, 7), (3, 8),
                           (4, 6), (4, 7), (4, 8),
                           (5, 6), (5, 7), (5, 8)],
                  (2, 0): [(6, 0), (6, 1), (6, 2),
                           (7, 0), (7, 1), (7, 2),
                           (8, 0), (8, 1), (8, 2)],
                  (2, 1): [(6, 3), (6, 4), (6, 5),
                           (7, 3), (7, 4), (7, 5),
                           (8, 3), (8, 4), (8, 5)],
                  (2, 2): [(6, 6), (6, 7), (6, 8),
                           (7, 6), (7, 7), (7, 8),
                           (8, 6), (8, 7), (8, 8)]
                  }

        combs = {}

        # initialize the combination dictionary which stores all possible
        # options for each place in board
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    combs[i, j] = {1: None, 2: None, 3: None, 4: None,
                                   5: None, 6: None, 7: None, 8: None, 9: None}

        # given that a board location has a value x, remove the possible value for
        # its neighbors. If at least one of the neighbors has no viable values,
        # return False. Else, return True
        def remove_value(i_current, j_current, value):
            # the following code is problematic
            # because we don't erase the removal
            # if the function returns False

            # 1st: check if this value is viable
            # check same row
            for jj in range(0, 9):
                if board[i_current][jj] != ".":
                    continue
                if value in combs[i_current, jj] and len(combs[i_current, jj]) == 1:
                    return False, []

            # check same column
            for ii in range(0, 9):
                if board[ii][j_current] != ".":
                    continue
                if value in combs[ii, j_current] and len(combs[ii, j_current]) == 1:
                    return False, []

            # check same sub-box
            for ii, jj in panels[i_current//3, j_current//3]:
                if board[ii][jj] != ".":
                    continue
                if value in combs[ii, jj] and len(combs[ii, jj]) == 1:
                    return False, []

            deleted = []

            # 2nd: if viable, then remove the value and return True
            # remove same row
            for jj in range(0, 9):
                if board[i_current][jj] != ".":
                    continue
                if value in combs[i_current, jj]:
                    deleted.append((i_current, jj))
                    del combs[i_current, jj][value]

            # remove same column
            for ii in range(0, 9):
                if board[ii][j_current] != ".":
                    continue
                if value in combs[ii, j_current]:
                    deleted.append((ii, j_current))
                    del combs[ii, j_current][value]

            # remove same sub-box
            for (ii, jj) in panels[i_current//3, j_current//3]:
                if board[ii][jj] != ".":
                    continue
                if value in combs[ii, jj]:
                    deleted.append((ii, jj))
                    del combs[ii, jj][value]

            return True, deleted

        # recover the removed value if this branch didn't work
        def recover_value(value, deleted_seqs):

            for (ii, jj) in deleted_seqs:
                combs[ii, jj][value] = None

        def fill_out(index):
            # recursion that fills out the board by index

            if index > 80:
                return True

            index_i = index // 9    # row
            index_j = index % 9     # column
            #if index_i == 4 and index_j == 1:
             #   print("break")

            # if this place has a given number then just
            # go to the next index
            if board[index_i][index_j] != ".":
                return fill_out(index+1)

            for key in combs[index_i, index_j]:
                board[index_i][index_j] = str(key)
                success, deleted_seq = remove_value(index_i, index_j, key)
                # print("keys checked: ", index_i, index_j, "key: ", key, success)
                if success:
                    if fill_out(index+1):
                        print("True", index_i, index_j)
                        return True
                    else:
                        recover_value(key, deleted_seq)
                board[index_i][index_j] = "."

            # print("False", index_i, index_j)
            return False

        # remove from combs the values that are not viable initially
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != ".":
                    remove_value(i, j, int(board[i][j]))

        fill_out(0)


sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

board2 = [[".", ".", ".", ".", ".", ".", "9", "5", "8"],
          [".", ".", ".", ".", ".", ".", "7", "1", "3"],
          [".", ".", ".", ".", "7", ".", "2", "6", "4"],
          ["4", "6", "8", "1", "2", "7", "3", "9", "5"],
          ["5", "9", "7", "4", "3", "8", "6", "2", "1"],
          ["1", "3", "2", "5", "9", "6", "4", "8", "7"],
          ["3", "2", "5", "7", "8", "9", "1", "4", "6"],
          ["6", "4", "1", "2", "5", "3", "8", "7", "9"],
          ["7", "8", "9", "6", "4", "1", "5", "3", "2"]]

for line in board:
    print(line)
sol.solveSudoku(board)
for line in board:
    print(line)

