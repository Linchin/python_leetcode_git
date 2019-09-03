"""
Q252
Meeting rooms
Easy

/sort/

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""
from typing import List
from itertools import chain

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        # sort
        sorted_time = sorted(intervals, key=lambda a:a[0])

        flatten = list(chain.from_iterable(sorted_time))

        for i in range(1, len(flatten)):

            if flatten[i] < flatten[i-1]:
                return False

        return True



time = [[25,30],[5,10],[15,20]]

sol = Solution()

print(sol.canAttendMeetings(time))

















