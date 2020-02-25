"""
Q139
Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing
a list of non-empty words, determine if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note:
1. The same word in the dictionary may be reused multiple times
   in the segmentation.
2. You may assume the dictionary does not contain duplicate words.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if not s:
            return True

        l = len(s)

        pairs = {}

        lengths = {}

        for word in wordDict:

            for i in range(0, l):
                j = i+len(word)
                if s[i:j] == word:
                    pairs[(i, j)] = True

            lengths[len(word)] = True

        dp_results = {}

        def dp(start):

            if start == l:
                return True

            if start in dp_results:
                return dp_results[start]

            for i in lengths:
                if (start, start+i) in pairs:
                    if dp(start+i) is True:
                        dp_results[i] = True
                        return True

            return False

        return dp(0)

sol = Solution()

s = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


print(sol.wordBreak(s, wordDict))

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]