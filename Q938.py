"""
Q938
Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum
of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def find_sum(root):
            if root is None:
                return 0
            if L <= root.val <= R:
                return root.val + find_sum(root.left) + find_sum(root.right)
            elif root.val < L:
                return find_sum(root.right)
            else:
                return find_sum(root.left)

        return find_sum(root)





