"""
Q039
Combination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates)
and a target number (target), find all unique combinations in
candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited
number of times.

Note:
1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        all_comb = []
        candidates = sorted(candidates)        # sorted makes it faster

        def find_comb(max_dig, comb):

            sum_comb = sum(comb)

            if max_dig == 0:
                i = 0
                while sum_comb + i * candidates[0] <= target:
                    if sum_comb + i * candidates[0] == target:
                        all_comb.append(comb+i*[candidates[0]])
                    i += 1
                return

            i = 0

            while i*candidates[max_dig] + sum_comb <= target:
                find_comb(max_dig-1, comb + [candidates[max_dig]] * i)
                i += 1

        find_comb(int(len(candidates)-1), [])

        return all_comb


sol = Solution()
candidates = [2,3,5]
target = 8
print(sol.combinationSum(candidates, target))






