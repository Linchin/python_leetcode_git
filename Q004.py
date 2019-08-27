"""
Q146 Median of Two Sorted Arrays
Hard
Done. :)

array; binary search; divide and conquer.

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        if m == 0:
            if n%2 == 1:
                return nums2[int((n+1)//2-1)]
            else:
                return (nums2[int((n+1)//2-1)] + nums2[int((n+1)//2)])/2
        if n == 0:
            if m%2 == 1:
                return nums1[int((m+1)//2-1)]
            else:
                return (nums1[int((m + 1) // 2 - 1)] + nums1[int((m + 1) // 2)]) / 2

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        l = 0
        h = m

        if (m + n) % 2 == 0:
            # even

            while 1:

                p1 = int((l + h) // 2)          # number of elements on the left
                p2 = int((m + n) / 2 - p1)

                if p1 == 0 and p2 == n:
                    return (nums1[0] + nums2[-1])/2

                if p1 == m and p2 == 0:
                    return (nums1[-1] + nums2[0]) / 2

                if p1 == m:
                    if nums1[-1] <= nums2[p2]:
                        print("a")
                        return (max(nums1[-1], nums2[p2-1]) + nums2[p2])/2
                    else:
                        h = p1
                        continue

                if p2 == n:
                    if nums2[-1] <= nums1[p1]:
                        return (max(nums2[-1], nums1[p1-1]) + nums1[p1])/2
                    else:
                        l = p1
                        continue

                left1 = nums1[p1-1]
                left2 = nums2[p2-1]
                right1 = nums1[p1]
                right2 = nums2[p2]

                if p1 == 0:
                    if left2 <= right1:
                        return (left2 + min(right1, right2))/2
                    else:
                        if l + 1 == h:
                            l = h
                            continue
                        else:
                            l = p1
                            continue

                if p2 == 0:
                    if left1 <= right2:
                        return (left1 + min(right1, right2))/2
                    else:
                        h = p1
                        continue

                if l+1 == h:
                    if left1 <= right2 and left2 <= right1:
                        return (max(left1, left2) + min(right1, right2)) / 2
                    else:
                        l = h
                        continue

                if left1 <= right2 and left2 <= right1:
                    return (max(left1, left2) + min(right1, right2))/2

                elif left1 >= right2:
                    h = p1
                    continue
                elif left1 <= right2:
                    l = p1
                    continue

        else:
            # odd

            while 1:

                p1 = int((l + h) // 2)  # number of elements on the left
                p2 = int((m + n + 1) / 2 - p1)

                if p1 == 0 and p2 == n:
                    if nums1[0] >= nums2[-1]:
                        return nums2[-1]
                    else:
                        l = h
                        continue

                if p1 == m and p2 == 0:
                    return nums1[-1]

                if p1 == m:
                    if nums1[-1] <= nums2[p2]:
                        return max(nums1[-1], nums2[p2-1])
                    else:
                        h = p1
                        continue

                if p2 == n:
                    if nums2[-1] <= nums1[p1]:
                        return max(nums1[p1-1], nums2[-1])
                    else:
                        l = p1
                        continue

                left1 = nums1[p1 - 1]
                left2 = nums2[p2 - 1]
                right1 = nums1[p1]
                right2 = nums2[p2]

                if p1 == 0:
                    if left2 <= right1:
                        return left2
                    else:
                        if l + 1 == h:
                            l = h
                            continue
                        else:
                            l = p1
                            continue

                if p2 == 0:
                    if left1 <= right2:
                        return (left1 + min(right1, right2)) / 2
                    else:
                        h = p1
                        continue

                if l + 1 == h:
                    if left1 <= right2 and left2 <= right1:
                        return max(left1, left2)
                    else:
                        l = h
                        continue

                if left1 <= right2 and left2 <= right1:
                    return max(left1, left2)

                elif left1 >= right2:
                    h = p1
                    continue
                elif left1 <= right2:
                    l = p1
                    continue




sol = Solution()

nums1 = [1]
nums2 = [2,5,6]


print(sol.findMedianSortedArrays(nums1, nums2))






