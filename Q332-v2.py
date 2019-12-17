"""
Q332 Reconstruct Itinerary
Medium
v2

10/10/2019

Given a list of airline tickets represented by pairs of
departure and arrival airports [from, to], reconstruct
the itinerary in order. All of the tickets belong to a
man who departs from JFK. Thus, the itinerary must begin
with JFK.

"""

from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        global tickets_sorted, count
        tickets_sorted = sorted(tickets, key=lambda item: (item[0], item[1]))
        itr = ["JFK"]
        used = {}
        total = len(tickets)

        while len(itr) <= total:
            i = 0
            while i < len(tickets_sorted):
                item = tickets_sorted[i]
                i += 1
                flag = 0
                if str(item) not in used and item[0] == itr[-1]:
                    itr.append(item[1])
                    used[str(item)] = 0

                    used = {k: v for k, v in used.items() if v == 0}
                    flag = 1
                    break
            if i == len(tickets_sorted) and flag == 0:
                used[str([itr[-2], itr[-1]])] = -1
                itr.pop()

        return itr


a = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],
     ["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

sol = Solution()

print(sol.findItinerary(a))


