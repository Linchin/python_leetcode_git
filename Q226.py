"""
Q226
Invert Binary Tree
Easy

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so f*** off.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def invert_(root) -> TreeNode:

            if root is None:
                return None

            root.left, root.right = root.right, root.left
            
            invert_(root.left)
            invert_(root.right)

            return root

        return invert_(root)


sol = Solution()

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a1.left = a2
a1.right = a3

def preorder(tree):
    if tree is not None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)

sol.invertTree(a1)
preorder(a1)