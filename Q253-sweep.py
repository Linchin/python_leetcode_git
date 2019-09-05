"""
Q 253
Meeting Rooms II
Medium

/Heap
Greedy
Sort/

Given an array of meeting time intervals consisting of start and
end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum
number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        total_room = 1

        end_time = [-1]

        sorted_start = sorted(intervals, key=lambda item: item[0])

        for item in sorted_start:

            if item[0] < min(end_time):
                total_room += 1
                end_time.append(item[1])

            else:
                index = end_time.index(min(end_time))
                end_time[index] = item[1]

        return total_room




a = [[0, 30],[5, 10],[15, 20]]
b = [[7,10],[2,4]]
c = [[7,10]]
d = []
sol = Solution()
print(sol.minMeetingRooms(d))
















