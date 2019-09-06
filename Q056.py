"""
Q056
Merge Intervals
Medium

20190905

/Array
Sort/

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []

        sorted_i = sorted(intervals, key=lambda i: i[0])
        merged = []
        current = sorted_i[0].copy()

        for item in sorted_i[1:]:
            if item[0] > current[1]:
                merged.append(current)
                current = item.copy()
            else:
                current[1] = max(current[1], item[1])

        merged.append(current)

        return merged



a = [[1,4],[2,3]]
sol = Solution()
print(sol.merge(a))











