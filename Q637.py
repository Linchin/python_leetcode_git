"""
Q637
Average of Levels in Binary Tree
Easy


Given a non-empty binary tree, return the average value of the
nodes on each level in the form of an array.
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        levels = []

        def read_level(root, d):
            if root is None:
                return
            if len(levels) < d:
                levels.append([])
            levels[d-1].append(root.val)
            read_level(root.left, d+1)
            read_level(root.right, d+1)

        read_level(root, 1)

        ave = []
        for val in levels:
            ave.append(sum(val)/len(val))

        return ave








