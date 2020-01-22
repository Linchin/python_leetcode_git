"""
Q235
Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common
ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants (where
we allow a node to be a descendant of itself).”

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        small = min(p.val, q.val)
        large = max(p.val, q.val)

        def find_ans(r):
            if small <= r.val <= large:
                return r
            elif r.val < small:
                return find_ans(r.right)
            else:
                return find_ans(r.left)

        return find_ans(root)
