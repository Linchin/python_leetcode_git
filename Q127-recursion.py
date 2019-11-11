"""
Q127 Word Ladder
Medium

11/11/2019

Topic:
BFS

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to
endWord, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that
beginWord is not a transformed word.

Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.
"""

from typing import List

class Solution:

    @staticmethod
    def canTransform(word1: str, word2: str) -> bool:
        # return True if word1 can be transformed into word2
        count = 0
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                count += 1

        if count == 0:
            return True
        else:
            return False

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        length = len(wordList)
        used_marker = [0] * length
        trans_string = []
        count = 0

        current = beginWord.copy()

        i = 0
        while(1):

            # ending condition
            if current == endWord:
                return count

            if used_marker[i] == 0 and self.canTransform(wordList[i],
                                                         current):
                count += 1
                current = wordList[i]
                used_marker[i] = 1
                trans_string.append(current)

            i += 1














