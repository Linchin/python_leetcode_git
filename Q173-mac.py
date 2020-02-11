"""
Q173
Binary Search Tree Iterator
Medium

Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note:
1. next() and hasNext() should run in average O(1) time and uses
O(h) memory, where h is the height of the tree.
2. You may assume that next() call will always be valid, that is,
there will be at least a next smallest number in the BST when
next() is called.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):

        self.q = [root]

    def next(self) -> int:
        """
        @return the next smallest number
        """

        def find_min(root_node):
            while root_node.left is not None:
                # given root, find min value of subtree
                self.q.append(root_node.left)
                root_node = root_node.left

        if self.q[-1].left is not None:
            find_min(self.q[-1])
            return self.q.pop().val

        elif self.q[-1].right is not None:
            to_be_returned = self.q.pop()
            find_min(to_be_returned.right)

            return to_be_returned.val

        else:

            return self.q.pop().val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.q) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


