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
        if root is not None:
            self.hasnext = True
        else:
            self.hasnext = False
        self.current = self.q[-1]
        while self.current.left is not None:
            self.current = self.current.left
            self.q.append(self.current)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.q:
            return None

        current = self.current

        # find the next smallest value
        if self.current.right is not None:
            self.q.append(self.current.right)
            self.current = self.q[-1]
            while self.current.left is not None:
                self.current = self.current.left
                self.q.append(self.current)
        else:
            if not self.q:
                self.hasnext = False
            else:
                self.current = self.q[-1]

        return current.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.hasnext


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


