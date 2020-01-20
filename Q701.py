"""
Q701
Insert into a Binary Search Tree
Medium

Given the root node of a binary search tree (BST) and a value
to be inserted into the tree, insert the value into the BST.
Return the root node of the BST after the insertion. It is
guaranteed that the new value does not exist in the original
BST.

Note that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can
return any of them.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def insert_(root, val):

            if root.left is None and root.right is None:
                if root.val > val:
                    root.left = TreeNode(val)
                else:
                    root.right = TreeNode(val)
                return None

            if root.val > val:
                if root.left is not None:
                    insert_(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right is not None:
                    insert_(root.right, val)
                else:
                    root.right = TreeNode(val)

            return None

        insert_(root, val)
        return root

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a2.left = a1
a2.right = a3

sol = Solution()

def preorder(tree):
    if tree is not None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)


sol.insertIntoBST(a2, 4)
preorder(a2)

