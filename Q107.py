"""
Q107
Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order
traversal of its nodes' values. (ie, from left to right,
level by level from leaf to root).
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]: