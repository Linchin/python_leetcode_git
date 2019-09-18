"""
Q091
Decode Ways
Medium

String; Dynamic programming.

A message containing letters from A-Z is being encoded to numbers
using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total
number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF"
(2 2 6).
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0

        t1 = 1
        t2 = 1
        t3 = 1

        for i in range(1, len(s)):

            t3 = 0

            # single
            if s[i] != "0":
                t3 += t2
            # double
            if "10" <= s[i-1:i+1] < "27":
                t3 += t1
            t1, t2 = t2, t3

        return t3

sol = Solution()
a = "1001"
print(sol.numDecodings(a))




