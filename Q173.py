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
        if not root:
            self.q = []
            return
        current = self.q[-1]
        while current.left is not None:
            current = current.left
            self.q.append(current)

    def next(self) -> int:
        """
        @return the next smallest number
        """

        current = self.q.pop()

        # find the next smallest value
        if current.right is not None:
            self.q.append(current.right)
            temp = self.q[-1]
            while temp.left is not None:
                temp = temp.left
                self.q.append(temp)

        return current.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.q) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

a1 = TreeNode(7)
a2 = TreeNode(3)
a3 = TreeNode(15)
a4 = TreeNode(9)
a5 = TreeNode(20)

a1.left = a2
a1.right = a3
a3.left = a4
a3.right = a5

iterator = BSTIterator(a1)
print(iterator.hasNext())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.next())
print(iterator.hasNext())

