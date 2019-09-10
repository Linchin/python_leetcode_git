"""
Q973
K Closest Points to origin
Medium

20190906
20190910 done

We have a list of points on the plane.  Find the K closest points
to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean
distance.)

You may return the answer in any order.  The answer is guaranteed
to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin,
so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        # calculate the distances from the points to the origin
        distance = {}
        for item in points:
            distance[(item[0], item[1])] = item[0]**2 + item[1]**2

        # private function: partition
        def partition(dis, current):
            count = 0
            eq_count = 0
            small = []
            large = []
            equal = []
            for item in current:
                if distance[(item[0], item[1])] < distance[(dis[0], dis[1])]:
                    count += 1
                    small.append(item)
                elif distance[(item[0], item[1])] > distance[(dis[0], dis[1])]:
                    large.append(item)
                else:
                    equal.append(item)
                    eq_count += 1

            return count, eq_count, small, large, equal

        par, eq, small, large, equal = partition(points[0], points)

        found = 0

        found_list = []

        while True:
            if par + found > K:
                par, eq, small, large, equal = partition(small[0], small)

            elif par + found + eq > K:
                return found_list+ small + equal[:K-par-found]

            elif par + found + eq == K:
                return found_list + small + equal

            else:
                found_list += small + equal
                found += par + eq
                par, eq, small, large, equal = partition(large[0], large)


sol = Solution()

points = [[1,3],[-2,2]]
points = [[3,3],[5,-1],[-2,4]]
points = [[0,1],[1,0]]
K = 2

print(sol.kClosest(points, K))
















