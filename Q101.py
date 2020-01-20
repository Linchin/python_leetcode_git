"""
Q101
Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of
itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
  / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # find the max depth
        def find_depth(root):
            if root is None:
                return 0
            else:
                return max(find_depth(root.left), find_depth(root.right)) + 1

        depth = find_depth(root)
        if depth == 0:
            return True

        left_nodes = [root.left]
        if root.left is None:
            left_val = [None]
        else:
            left_val = [root.left.val]
        right_nodes = [root.right]
        if root.right is None:
            right_val = [None]
        else:
            right_val = [root.right.val]
        for i in range(depth):
            if left_val != right_val[::-1]:
                return False
            else:
                left_temp = []
                for left, right in zip(left_nodes, right_nodes):
                    if item is None:
                        left_temp.append(None)
                        left_temp.append(None)
                    else:
                        left_temp.append(item.left)
                        left_temp.append(item.right)
                left_val = []
                left_nodes = left_temp
                for item in left_nodes:
                    if item is None:
                        left_val.append(None)
                    else:
                        left_val.append(item.val)

                right_temp = []
                for item in right_nodes:
                    if item is None:
                        right_temp.append(None)
                        right_temp.append(None)
                    else:
                        right_temp.append(item.left)
                        right_temp.append(item.right)
                right_val = []
                right_nodes = right_temp
                for item in right_nodes:
                    if item is None:
                        right_val.append(None)
                    else:
                        right_val.append(item.val)
        return True

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)

a2.left = a1
a2.right = a3

sol = Solution()
print(sol.isSymmetric(a2))


