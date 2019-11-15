"""
Q1007
Minimum Domino Rotations For Equal Row
Medium

Array; greedy.

In a row of dominoes, A[i] and B[i] represent the top and
bottom halves of the i-th domino.  (A domino is a tile with
two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the
values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Note:
1. 1 <= A[i], B[i] <= 6
2. 2 <= A.length == B.length <= 20000

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
"""
from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        L = len(A)

        flips = [0] * 6 # number of flips required for each number 1-6
        for j in range(1, 7):
            flipA = 0
            flipB = 0
            for i in range(0, L):
                if A[i] == j and B[i] == j:
                    continue
                elif A[i] != j and B[i] == j:
                     flipA += 1
                elif A[i] == j and B[i] != j:
                    flipB += 1
                else:
                    flips[j-1] = -1     # no way we can form a row of value j
                    break
            if flips[j-1] == 0:
                flips[j-1] = min(flipA, flipB)

        if max(flips) == -1:
            return -1
        else:
            new_flips = [item for item in flips if item != -1]
            return min(new_flips)

def run():
    sol = Solution()
    A = [3,5,1,2,3]
    B = [3,6,3,3,4]
    print(sol.minDominoRotations(A, B))


if __name__ == "__main__":
    # do something if this script is invoked
    # as python scriptname. Otherwise, gets ignored.

    import cProfile
    cProfile.run('run()')

