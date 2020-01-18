"""
Q392
Is Subsequence
Easy

:Dynamic Programming:

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in
both s and t. t is potentially a very long (length ~= 500,000)
string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from
the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the
remaining characters. (ie, "ace" is a subsequence of "abcde"
while "aec" is not).


Notes:
No need for DP; There is no need for backtracking, so we just move
along.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in range(0, len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s):
                return True
        return False

class Solution2:
    # pop didnt work since string doesnt do pop
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        while t:
            if t[-1] == s[-1]:
                s.pop()
                t.pop()
            else:
                t.pop()
            if not s:
                return True

        return False

s = "abc"
t = "ahbgd"
sol = Solution2()
print(sol.isSubsequence(s, t))