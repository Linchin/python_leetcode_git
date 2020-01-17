"""
Q104
Max Depth of Binary Tree
Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def find_depth(root) -> int:
            if root is None:
                return 0
            left = find_depth(root.left)
            right = find_depth(root.right)
            return max(left, right) + 1

        return find_depth(root)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
b.left = d

sol = Solution()
print(sol.maxDepth(d))




