"""
Leetcode Question #146
LRU Cache

Author: Lingqing Gan
Date: 08/06/2019

Question:
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

notes:
linked list + dict(hash map)
"""


class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.hash = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        # if the inquired node is the last/only node
        if self.hash[key].next is None:
            return self.hash[key].val

        # AT LEAST 2 NODES
        # move the inquired node to the end of the linked list

        # handle head and tail of the linked list
        if self.head == self.hash[key]:
            self.head = self.head.next
        last = self.tail.key
        self.tail.next = self.hash[key]
        self.tail = self.hash[key]

        # connect the nodes before and after the inquired node
        if self.hash[key].prev is not None:
            self.hash[key].prev.next = self.hash[key].next
        if self.hash[key].next is not None:
            self.hash[key].next.prev = self.hash[key].prev

        # update the prev/next node of the inquired node
        self.hash[key].prev = self.hash[last]
        self.hash[key].next = None

        return self.hash[key].val

    def put(self, key: int, value: int) -> None:

        # if the key exists
        if key in self.hash:
            self.hash[key].val = value
            self.get(key)
            return 0

        # if key is new
        self.hash[key] = self.Node(key, value)

        if self.size == 0:
            # first node
            self.head = self.tail = self.hash[key]
            self.size = 1
        elif self.size < self.cap:
            # capacity not reached, just add new node to the end
            self.tail.next = self.hash[key]
            self.hash[key].prev = self.tail
            self.tail = self.hash[key]
            self.size += 1
        else:
            # capacity reached, need to remove LRU node
            self.tail.next = self.hash[key]
            self.hash[key].prev = self.tail
            self.tail = self.hash[key]
            first = self.head.key
            self.head = self.head.next
            self.head.prev = None
            del self.hash[first]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

capacity = 2
cache = LRUCache(capacity)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))




