"""
Q1000
Minimum Cost to Merge Stones
Hard

There are N piles of stones arranged in a row.
The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles
into one pile, and the cost of this move is equal to
the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones
into one pile.  If it is impossible, return -1.


"""

from typing import List
import functools

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:

        n = len(stones)

        if n == 1:
            return 0

        if K == 1:
            return -1

        if (n-1) % (K-1) != 0:
            return -1

        if n == K:
            return sum(stones)

        incre = [0] * (n+1)
        for ii in range(0, n):
            incre[ii+1] = incre[ii] + stones[ii]

        @functools.lru_cache(None)
        def dp(i, j, k):

            if k == 1:
                if j - i + 1 == K:
                    return incre[j+1]-incre[i]
                elif j == i:
                    return 0
                elif j-i+1 < K:
                    return float('inf')
                else:
                    return min(dp(i, mid, 1) + dp(mid + 1, j, K-1) for mid in range(i, j)) + incre[j+1] - incre[i]
            else:
                if j-i+1 == k:
                    return 0
                if j - i + 1 <= K:
                    return float('inf')
                return min(dp(i, mid, 1) + dp(mid+1, j, k-1) for mid in range(i, j))

        res = min(dp(0, mid, 1) + dp(mid+1, n-1, K-1) for mid in range(0, n)) + incre[n]

        return res


sol = Solution()
stones = [22,91,24,26,21,100,42,23,56,64,43,95,76,84,79,89]
K = 6
print(sol.mergeStones(stones, K))




