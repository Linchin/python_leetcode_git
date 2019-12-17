"""
Q1065
Index Pairs of a String
Easy

virtual test.
"""
from typing import List

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(0, len(text)):
            for j in range(i, len(text)):
                if text[i:j+1] in words:
                    pairs.append([i,j])
        return pairs

text = "thestoryofleetcodeandme"
words = ["story","fleet","leetcode"]

sol = Solution()
print(sol.indexPairs(text, words))