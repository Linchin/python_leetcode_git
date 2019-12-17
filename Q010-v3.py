"""
Q010
Regular Expression Matching
Hard

string; DP; backtracking.

v3
DP from Leetcode solution.

Given an input string (s) and a pattern (p), implement
regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the ENTIRE input string (not partial).

Note:
1. s could be empty and contains only lowercase letters a-z.
2. p could be empty and contains only lowercase letters a-z,
    and characters like . or *.

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".
"""

class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)