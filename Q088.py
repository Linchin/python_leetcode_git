"""
Q088
Merge Sorted Array
Easy

/array
two pointers/

...
Need to merge in place.

```

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

* The number of elements initialized in nums1 and nums2 are m and n respectively.
* You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, end = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:

            if nums1[i] >= nums2[j]:

                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1

            end -= 1

        if j >= 0:

            nums1[:j+1] = nums2[:j+1]



nums1 = [0]
m = 0
nums2 = [6]
n = 1

sol = Solution()

sol.merge(nums1, m, nums2, n)

print(nums1)








