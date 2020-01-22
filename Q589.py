"""
Q589
N-ary Tree Preorder Traversal
Easy

Given an n-ary tree, return the preorder traversal of its
nodes' values.

Nary-Tree input serialization is represented in their level
order traversal, each group of children is separated by the
null value (See examples).


Follow up:
Recursive solution is trivial, could you do it iteratively?

"""

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if root is None:
            return []

        stack = [root]

        preo = []

        while stack:
            current = stack.pop()
            preo.append(current.val)
            children = current.children
            while children:
                stack.append(children.pop())

        return preo

