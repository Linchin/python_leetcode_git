"""
Q072
Edit Distance
Hard


Given two words word1 and word2, find the minimum number of
operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        l1 = len(word1) + 1
        l2 = len(word2) + 1

        D = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(l1):
            D[i][0] = i

        for j in range(l2):
            D[0][j] = j

        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    D[i][j] = 1 + min(D[i][j-1], D[i-1][j], D[i-1][j-1]-1)
                else:
                    D[i][j] = 1 + min(D[i][j-1], D[i - 1][j], D[i - 1][j - 1])

        return D[-1][-1]

sol = Solution()
word1 = "horse"
word2 = "ros"
print(sol.minDistance(word1, word2))












