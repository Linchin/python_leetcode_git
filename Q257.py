"""
Q257
Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_rec:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []

        def rec(root, path):
            path += str(root.val)
            if root.left is None and root.right is None:
                res.append(path)
                return
            if root.left is not None:
                rec(root.left, path+"->")
            if root.right is not None:
                 rec(root.right, path+"->")

        rec(root, "")
        return res

class Solution_it:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        stack = [(root, "")]
        res = []

        while stack:
            root, path = stack.pop()
            path += str(root.val)
            if root.left is None and root.right is None:
                res.append(path)
            if root.left is not None:
                stack.append((root.left, path+"->"))
            if root.right is not None:
                stack.append((root.right, path+"->"))

        return res



sol = Solution_rec()

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.left = node2
node1.right = node3
node2.left = node4

print(sol.binaryTreePaths(node1))

sol2 = Solution_it()
print(sol2.binaryTreePaths(node1))


























