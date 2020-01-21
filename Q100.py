"""
Q100
Same Tree
Easy

Given two binary trees, write a function to check if they are
the same or not.

Two binary trees are considered the same if they are structurally
identical and the nodes have the same value.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def same_(p, q):
            if p is None and q is None:
                return True
            elif (p is None and q is not None) or (
                p is not None and q is None
            ):
                return False
            elif p.val != q.val:
                return False
            else:
                return same_(p.left, q.left) and same_(p.right, q.right)

        return same_(p, q)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(1)

a1.left = a2
a1.right = a3

b1 = TreeNode(1)
b2 = TreeNode(2)
b3 = TreeNode(1)

b1.left = b2
b1.right = b2

sol = Solution()
print(sol.isSameTree(a1, b1))