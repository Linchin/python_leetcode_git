"""
Q079 Word Search

See also: Q212 Word Search II

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS search.
        """
        self.m = len(board)
        self.n = len(board[0])
        self.l = len(word)
        self.lc = 0

        self.word = word
        self.board = board

        self.q = []

        return self.search()

    def search(self):
        """
        Recursion. DFS.
        """

        if self.lc == self.l:
            return True

        if self.lc == 0:
            for i in range(0, self.m):
                for j in range(0, self.n):
                    if self.board[i][j] == self.word[self.lc]:
                        self.q.append((i, j))
                        self.lc += 1
                        if self.search():
                            return True
                        else:
                            self.lc -= 1
                            self.q.pop()
            return False

        current = self.word[self.lc]

        i = self.q[-1][0]
        j = self.q[-1][1]

        i1, j1 = i, j + 1
        i2, j2 = i, j - 1
        i3, j3 = i + 1, j
        i4, j4 = i - 1, j

        if 0 <= i1 < self.m and 0 <= j1 < self.n \
                and self.board[i1][j1] == current\
                and (i1, j1) not in self.q:
            self.q.append((i1, j1))
            self.lc += 1
            if self.search():
                return True
            self.lc -= 1
            self.q.pop()

        if 0 <= i2 < self.m and 0 <= j2 < self.n \
                and self.board[i2][j2] == current\
                and (i2, j2) not in self.q:
            self.q.append((i2, j2))
            self.lc += 1
            if self.search():
                return True
            self.lc -= 1
            self.q.pop()

        if 0 <= i3 < self.m and 0 <= j3 < self.n \
                and self.board[i3][j3] == current \
                and (i3, j3) not in self.q:
            self.q.append((i3, j3))
            self.lc += 1
            if self.search():
                return True
            self.lc -= 1
            self.q.pop()

        if 0 <= i4 < self.m and 0 <= j4 < self.n \
                and self.board[i4][j4] == current \
                and (i4, j4) not in self.q:
            self.q.append((i4, j4))
            self.lc += 1
            if self.search():
                return True
            self.lc -= 1
            self.q.pop()

        return False

sol = Solution()

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABC"

print(sol.exist(board, word))




