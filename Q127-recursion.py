"""
Q127 Word Ladder
Medium

11/11/2019

Topic:
BFS

11/11 notes:
strange thing:
for the case:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

My code returned 0 on my local computer. It says 0 in run-code.
But it returns 5 if I submit.


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

    trans_lengths = []

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

    def find_next(self,
                  current_word: str,
                  endWord: str,
                  word_list: List[str],
                  cnt: int):

        for item in word_list:
            if self.canTransform(current_word, item):
                if item == endWord:
                    self.trans_lengths.append(cnt+1)
                    continue
                else:
                    new_list = word_list.copy()
                    new_list.remove(item)
                    self.find_next(item, endWord, new_list, cnt+1)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        self.find_next(beginWord, endWord, wordList, 1)
        if len(self.trans_lengths) == 0:
            return 0
        else:
            return min(self.trans_lengths)

beginWord = "h"
endWord = "n"
wordList = ["c"]

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))












