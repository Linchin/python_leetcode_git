"""
Q617
Merge Two Binary Trees
Easy

Given two binary trees and imagine that when you put one
of them to cover the other, some nodes of the two trees
are overlapped while the others are not.

You need to merge them into a new binary tree. The merge
rule is that if two nodes overlap, then sum node values
up as the new value of the merged node. Otherwise, the
NOT null node will be used as the node of new tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def merge(t1: TreeNode, t2: TreeNode) -> TreeNode:

            if t1 is None and t2 is None:
                return None

            sum_ = 0

            left1 = None
            left2 = None
            right1 = None
            right2 = None

            if t1 is not None:
                sum_ += t1.val
                left1 = t1.left
                right1 = t1.right

            if t2 is not None:
                sum_ += t2.val
                left2 = t2.left
                right2 = t2.right

            new_node = TreeNode(sum_)
            new_node.left = merge(left1, left2)
            new_node.right = merge(right1, right2)

            return new_node

        return merge(t1, t2)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

b1 = TreeNode(5)
b2 = TreeNode(5)
b3 = TreeNode(5)

#a1.left = a2
a1.right = a3

b1.left = b2
b1.right = b3

sol = Solution()
tree = sol.mergeTrees(a1, b1)

def preorder(tree):
    if tree is not None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)

preorder(tree)





