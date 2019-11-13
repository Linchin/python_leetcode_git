"""
Q127 Word Ladder
Medium

11/11/2019

Topic:
BFS

V1: written using recursion

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

        if count == 1:
            return True
        else:
            return False

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        length = len(wordList)
        trans_sequence = [(beginWord, None)]
        trans_usage = {}       # 0: not in use, 1: in use

        for item in wordList:
            trans_usage[item] = 0

        while len(trans_sequence) > 0:

            current = trans_sequence[-1][0]

            i = 0
            while i < length:
                for j in range(0, length):
                    if trans_usage[wordList[j]] == 0 and self.canTransform(current,
                                                                           wordList[j]):
                        trans_sequence.append((wordList[i],i))
                        trans_usage[wordList[i]] = 1
                        current = wordList[i]
                        i = 0
                    elif trans_usage[wordList[i]] == 0 and endWord == wordList[i]:
                        return len(trans_sequence)+1
                    else:
                        i += 1

            _, i = trans_sequence.pop()
            trans_usage[wordList[i]] = 0
            i += 1

        return 0

sol = Solution()

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

print(sol.ladderLength(beginWord=beginWord, endWord=endWord, wordList=wordList))
















