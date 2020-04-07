"""
Q983
Minimum cost for tickets
Medium
In a country popular for train travel, you have planned some
train travelling one year in advance.  The days of the year
that you will travel is given as an array days.  Each day
is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For
example, if we get a 7-day pass on day 2, then we can travel
for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel
every day in the given list of days.

"""

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        min_price = [0] * 366

        def cost(index):
            if index > 365:
                return 0
            else:
                return min_price[index]

        for item in days:
            min_price[item] = -1

        if days[-1] == 365:
            min_price[-1] = costs[0]

        for i in reversed(range(1, 365)):

            if min_price[i] == 0:
                min_price[i] = min_price[i+1]
            else:
                min_price[i] = min(costs[0] + cost(i+1),
                                   costs[1] + cost(i+7),
                                   costs[2] + cost(i+30)
                                   )

        return min_price[1]

sol = Solution()
days = [1,4,6,7,8,365]
costs = [2,7,15]

print(sol.mincostTickets(days, costs))














