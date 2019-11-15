"""
Q332 Reconstruct Itinerary
Medium
v2

DFS; graph

11/15/2019 revisit
iterative.

Given a list of airline tickets represented by pairs of
departure and arrival airports [from, to], reconstruct
the itinerary in order. All of the tickets belong to a
man who departs from JFK. Thus, the itinerary must begin
with JFK.

Notes:
1.  If there are multiple valid itineraries, you should return
    the itinerary that has the smallest lexical order when read
    as a single string. For example, the itinerary ["JFK", "LGA"]
    has a smaller lexical order than ["JFK", "LGB"].
2.  All airports are represented by three capital letters (IATA code).
3.  You may assume all tickets form at least one valid itinerary.

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        legs = defaultdict(list)
        itr = ["JFK"]
        stack = ["JFK"]
        L = len(tickets)

        # connectivity info stored in dict
        for item in tickets:
            legs[item[0]].append(item[1])

        current = "JFK"
        while len(itr) != L+1:
            current = stack.pop()
            for item in sorted(legs[current]):
                itr.append(item)



        return itr


a = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],
     ["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

sol = Solution()

print(sol.findItinerary(a))


