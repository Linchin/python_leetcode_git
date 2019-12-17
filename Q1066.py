"""
Q1066
Campus Bikes II
Medium

from virtual contest
12/17/2019

bianli tree
"""
from typing import List
from itertools import permutations

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        N = len(workers)
        M = len(bikes)

        dist_dict = {}
        for i in range(0, N):
            for j in range(0, M):
                dist_dict[i, j] = abs(workers[i][0] - bikes[j][0]) + \
                                  abs(workers[i][1] - bikes[j][1])

        def dist_cal(pairs: List):
            # return the total Manhattan distance given the pairing
            total = 0
            for i in range(0, N):
                total += dist_dict[i, pairs[i]]
            return total

        min_dist = None

        for perm in permutations(range(0, M), N):
            if not min_dist:
                min_dist = dist_cal(perm)
            else:
                min_dist = min(min_dist, dist_cal(perm))

        return min_dist



sol = Solution()
workers = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]

print(sol.assignBikes(workers, bikes))



