"""
Q199: medium
Binary tree right side view.
Status: finished :)

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_view = []
        level_1 = []

        if not root:        # empty tree
            return right_view
        else:
            right_view.append(root.val)
            if root.left:
                level_1.append(root.left)
                next_level = 1
            if root.right:
                level_1.append(root.right)
                next_level = 1
            if not level_1:
                return right_view

        right_view.append(level_1[-1].val)

        while(next_level):
            next_level = 0
            level_2 = []

            # BFS
            for node in level_1:
                if node.left:
                    level_2.append(node.left)
                    next_level = 1
                if node.right:
                    level_2.append(node.right)
                    next_level = 1

            if next_level:# find right side view if next level exists
                right_view.append(level_2[-1].val)
                level_1 = level_2.copy()

        return right_view


