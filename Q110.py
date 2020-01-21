"""
Q110
Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every
node differ in height by no more than 1.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def isb(root):
            if root is None:
                return True, 0

            left, ld = isb(root.left)
            right, rd = isb(root.right)

            if abs(ld-rd) > 1:
                return False, -1

            return [left and right, max(ld, rd) + 1]

        return isb(root)[0]
