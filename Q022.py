"""
Q022
Generate Parenthesis
Medium

20190905
This method uses partition.
But it didn't work.


/String
Backtracking/

Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())", ***
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List


class Solution:

    partition = []

    def generateParenthesis(self, n: int) -> List[str]:

        seq = []

        self.find_partition(n, seq.copy())

        brackets_list = self.generate_brackets(self.partition)

        return brackets_list

    def find_partition(self, n, seq):
        # total number left

        if n == 0:
            self.partition.append(seq)

        for i in range(1, n+1):
            seq.append(i)
            self.find_partition(n-i, seq.copy())
            seq.pop()

    @staticmethod
    def generate_brackets(partition):

        s = []

        for i in partition:
            si = ""
            for j in i:
                si += "("*j + ")"*j
            s.append(si)

        return s

sol = Solution()
print(sol.generateParenthesis(3))










