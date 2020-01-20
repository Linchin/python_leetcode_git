"""
Q285
In Order Successor in BST
Medium

Given a binary search tree and a node in it, find the
in-order successor of that node in the BST.

The successor of a node p is the node with the smallest
key greater than p.val.

Note:

If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        # search for value in BST
        def find_(root, val):
            if root.val == val:
                return root
            elif root.val > val:
                return find_(root.left, val)
            else:
                return find_(root.right, val)

        # find the min value of a BST
        def find_min(root):
            if root is None:
                return None
            if root.left is None:
                return root.val
            else:
                return find_min(root.left)

        # find the inorder successor given the root
        def find_suc(root):
            return find_min(root.right)

        # find the node
        node = find_(root, p.val)

        # find the successor
        return find_suc(node)


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a2.left = a1
a2.right = a3

sol = Solution()

print(sol.inorderSuccessor(a2, a2))



