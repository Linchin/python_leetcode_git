"""
Q669
Trim a Binary Tree
Easy

Given a binary search tree and the lowest and highest boundaries
as L and R, trim the tree so that all its
elements lies in [L, R] (R >= L). You might need to change the
root of the tree, so the result should return the new root of
the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


#Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def trim_(root) -> TreeNode:

            # ending condition
            if root is None:
                return None

            if L <= root.val <= R:
                root.left = trim_(root.left)
                root.right = trim_(root.right)
                return root

            elif root.val < L:
                return trim_(root.right)

            else:
                return trim_(root.left)


        return trim_(root)

def preorder(tree):
    if tree is not None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)

L = 1
R = 2
a1 = TreeNode(1)
a2 = TreeNode(0)
a3 = TreeNode(2)
a1.left = a2
a1.right = a3



sol = Solution()

sol.trimBST(a1, L, R)
preorder(a1)

b1 = TreeNode(3)
b2 = TreeNode(0)
b3 = TreeNode(4)
b4 = TreeNode(2)
b5 = TreeNode(1)

b1.left = b2
b1.right = b3
b2.right = b4
b4.left = b5

L2 = 1
R2 = 3
sol.trimBST(b1, L2, R2)
preorder(b1)
