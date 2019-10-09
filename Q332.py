"""
Q332 Reconstruct Itinerary
Medium

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
        total = len(tickets)

        def find_next():
            global tickets_sorted, count
            # condition for true result
            if len(itr) == total+1:
                return True

            for i in range(0, len(tickets_sorted)):
                if tickets_sorted[i][0] == itr[-1]:
                    tickets_sorted.remove(tickets_sorted[i])
                    itr.append(tickets_sorted[i])
                    if find_next():
                        return True
                    else:
                        itr.pop()
                        tickets_sorted.append(tickets_sorted[i])
                        tickets_sorted = sorted(tickets, key=lambda item: (item[0], item[1]))
            return False

        find_next()
        return itr

a = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

sol = Solution()

print(sol.findItinerary(a))


