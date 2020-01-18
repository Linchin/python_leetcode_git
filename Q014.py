"""
Q014
Longest Common Prefix
Easy

:string:

Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:
All given inputs are in lowercase letters a-z.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common = ""

        min_length = len(strs[0])
        min_index = 0
        for i in range(0, len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                min_index = i

        for i in range(0, len(strs[min_index])):
            flag = True
            for j in range(0, len(strs)):
                if strs[j][i] != strs[0][i]:
                    flag = False
                    break
            if flag:
                common += strs[0][i]
            else:
                break
        return common

sol = Solution()
strs = ["aa","a"]
print(sol.longestCommonPrefix(strs))
