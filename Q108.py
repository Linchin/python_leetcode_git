"""
Q108
Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

"""

from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def to_bst(nums):

            if len(nums) == 0:
                return None

            mid = math.floor(len(nums) / 2)

            new_node = TreeNode(nums[mid])
            new_node.left = to_bst(nums[:mid])
            new_node.right = to_bst(nums[mid+1:])

            return new_node

        return to_bst(nums)