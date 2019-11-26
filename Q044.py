"""
Q044
Wildcard Matching
Hard

string; DP; Backtracking; Greedy

Given an input string (s) and a pattern (p), implement wildcard pattern
matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
1. s could be empty and contains only lowercase letters a-z.
2. p could be empty and contains only lowercase letters a-z, and
characters like ? or *.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not p:
            return not s

        memo = {}

        # preprocess p
        p_new = p[0]
        for i in range(1, len(p)):
            if p_new[-1] == "*" == p[i]:
                continue
            else:
                p_new += p[i]

        p = p_new

        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]

            if j == len(p):
                ans = i == len(s)
            elif i == len(s):
                ans = j == len(p) or all([p[jj] == "*" for jj in range(j, len(p))])
            elif p[j] in {"?", s[i]}:       # this one matches
                ans = dp(i+1, j+1)
            elif p[j] == "*":
                # ans = False
                # for ii in reversed(range(i, len(s)+1)):
                #     if dp(ii, j+1):
                #         ans = True
                #         break

                #if ii == len(s):
                #    ans = False
                ans = any([dp(ii, j+1) for ii in range(i, len(s)+1)])
            else:
                ans = False

            memo[i, j] = ans
            return memo[i,j]

        return dp(0, 0)

s = "aa"
p = "a"

s1 = "bbbabaaabaababbbbabbbbababbbabbbbaaabaaaabaaabaabbbaabbbbaababbbabbbbabbbbbbabbbbaabababaaaaabbaaabbaaabaababaaabaabbaabbabbaababaabaabaaabaababbaaabaaabbbbaabbabaaabbabaaabbbabaaaaaababaababbbbabbbaab"
p1 = "****aab**ba***bb***a*a*bab***b***ab*a*b*a***a******a*bb**a**bbaa*ba*abba*****b*aaba****a*b*****ba**abba"

def main():
    sol = Solution()
    print(sol.isMatch(s1, p1))

import cProfile
cProfile.run("main()")



