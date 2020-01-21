"""
Q543
Diameter of Binary Tree
Easy

Given a binary tree, you need to compute the length of
the diameter of the tree. The diameter of a binary tree
is the length of the longest path between any two nodes
in a tree. This path may or may not pass through the root.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def diameter(root):
            if root is None:
                return 0, 0
            dia_left, dep_left = diameter(root.left)
            dia_right, dep_right = diameter(root.right)
            return max(dia_left, dia_right, dep_left + dep_right), max(dep_left, dep_right) + 1

        return diameter(root)[0]


