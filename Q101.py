"""
Q101
Symmetric Tree
Easy

[iterative solution]

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

        if depth == 0 or depth == 1:
            return True

        left_nodes = [root.left]
        right_nodes = [root.right]

        for i in range(depth):
            left_next = []
            right_next = []

            for left, right in zip(left_nodes, right_nodes):

                if (left is None and right is not None) or (
                 left is not None and right is None):
                    return False

                elif left is None and right is None:
                    left_next.append(None)
                    left_next.append(None)
                    right_next.append(None)
                    right_next.append(None)

                else:
                    if left.val != right.val:
                        return False
                    else:
                        left_next.append(left.left)
                        left_next.append(left.right)
                        right_next.append(right.right)
                        right_next.append(right.left)

            right_nodes = right_next
            left_nodes = left_next

        return True


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(1)

a2.left = a1
a2.right = a3

sol = Solution()
print(sol.isSymmetric(a2))


