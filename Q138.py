"""
Q138
Copy List with Random Pointer
Medium

Hash table; Linked list.

A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},
"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


Note:

You must return the copy of the given head as a reference to the cloned list.

"""

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        buffer = {}
        start = Node(None, None, None)
        last = start
        while head:
            if head.val not in buffer:
                new_node = Node(head.val, head.next, head.random)
                buffer[head.val] = new_node
            else:
                new_node = buffer[head.val]

            if head.random:
                if head.random.val not in buffer:
                    new_ref_node = Node(head.random.val, None, None)
                    buffer[new_ref_node.val] = new_ref_node
                else:
                    new_ref_node = buffer[head.random.val]
            else:
                new_ref_node = None

            new_node.random = new_ref_node
            new_node.next = None
            last.next = new_node

            last = last.next
            head = head.next

        return start.next


sol = Solution()
node2 = Node(2, None, None)
node2.random = node2
node1 = Node(1, None, None)


copy = sol.copyRandomList(node1)

while node1 != None:
    print(node1.val, node1.random.val)
    node1 = node1.next
