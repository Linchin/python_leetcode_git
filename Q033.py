"""
Q033
Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


1. find the pivot number
2. do the search

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        lo = 0
        hi = len(nums)-1
        mid = (lo+hi)//2

        # find the index of the min value
        while(1):
            if nums[lo] < nums[hi]:
                # no rotation
                pivot = 0
                break
            elif nums[mid] > nums[lo] and nums[mid] > nums[mid+1]:
                # mid is max
                pivot = mid + 1
                break
            elif nums[mid] < nums[hi] and nums[mid] < nums[mid-1]:
                # mid is min
                pivot = mid
                break
            elif nums[mid] > nums[lo]:
                # mid is on the big side
                lo = mid
                mid = (lo+hi)//2
                continue
            elif nums[mid] < nums[hi]:
                # mid is on the small side
                hi = mid
                mid = (lo+hi)//2
                continue
            else:
                print("Value error in search for the pivot point!")
                exit(-1)

        # find the target value
        total_leng = len(nums)
        leng = len(nums)
        lo = pivot
        hi = (pivot - 1) % total_leng

        mid = (2*lo+leng)//2%total_leng

        while(1):

            if target == nums[mid]:
                return mid
            elif target == nums[lo]:
                return lo
            elif target == nums[hi]:
                return hi
            elif hi-lo == 1 or hi == lo or (hi==0 and lo==total_leng-1):
                return -1
            elif target > nums[mid]:
                lo = mid
                leng = (hi - lo) % total_leng
                mid = (2 * lo + leng)//2 % total_leng
                continue
            elif target < nums[mid]:
                hi = mid
                leng = (hi - lo) % total_leng
                mid = (2 * lo + leng)//2 % total_leng
                continue



a = [1,4,5]

sol = Solution()
print(sol.search(a, 5))









