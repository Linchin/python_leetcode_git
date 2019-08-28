"""
Q005 Longest Palindromic Substring

Medium

08/27/2019
home. Linear programming.
O(n^2)

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = len(s)

        if length == 0:
            return ""
        table = []

        for i in range(0, length):
            table.append([0] * (length-i))

        for i in range(1, length+1):            # length of the palindrome
            for j in range(0, length-i+1):      # index of the beginning character

                if i == 1 or \
                   s[j] == s[i+j-1] and i == 2 or\
                   (s[j] == s[i+j-1] and table[i-3][j+1]):
                    table[i-1][j] = True
                    max_s = s[j:j+i]

        return max_s

a = "a"
sol = Solution()
print(sol.longestPalindrome(a))















