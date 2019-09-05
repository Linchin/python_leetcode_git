"""
Q022
Generate Parenthesis
Medium

20190905
2nd try after learning backtracking.

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
    def generateParenthesis(self, n: int) -> List[str]:

        a = []

        def generate(p, l, r):

            # l: how many left parens are left
            # r: how many right parens are left

            if l == 0:
                a.append(p+")"*r)
                return 0

            elif l > r:
                return 0

            else:
                generate(p+"(", l-1, r)
                generate(p+")", l, r-1)

        generate("", n, n)

        return a


sol = Solution()
print(sol.generateParenthesis(4))


