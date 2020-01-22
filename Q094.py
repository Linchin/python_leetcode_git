"""
Q094
Binary Tree Inorder Traversal
Medium

Given a binary tree, return the inorder traversal of its
nodes' values.

Follow up:
Recursive solution is trivial, could you do it iteratively?
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

