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

    def add(self, key: int, value: int):
        # add a node to the end
        self.hash[key] = self.Node(key, value)
        self.tail = self.hash[key]
        self.size += 1

    def remove(self, key: int):
        # remove a node
        # if the node is 1st
        if self.hash[key].prev is None:
            self.size -= 1
            self.head = self.hash[key].next
        # if the node is last
        elif self.hash[key].next is None:
            self.size -= 1
            self.head = self.hash[key].prev
        # if the node is in the middle
        else:
            self.size -= 1
            self.hash[key].prev.next = self.hash[key].next
            self.hash[key].next.prev = self.hash[key].prev
        # remove the node from hash table
        del self.hash[key]

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        # move the inquired node to the last of the linked list
        if self.hash[key].prev is not None:
            self.hash[key].prev.next = self.hash[key].next
        if self.hash[key].next is not None:
            self.hash[key].next.prev = self.hash[key].prev
        self.tail.next = self.hash[key]
        self.hash[key].next = None
        self.hash[key].prev = self.tail
        self.tail = self.hash[key]
        return self.hash[key].val

    def put(self, key: int, value: int) -> None:
        self.hash[key] = self.Node(key, value)
        if self.size < self.cap:
            # capacity not reached, just add new node
            if self.tail is not None:
                self.tail.next = self.hash[key]
                self.hash[key].prev = self.tail
            self.tail = self.hash[key]
            self.size += 1
        else:
            # capacity reached, need to remove LRU node
            if self.tail is not None:
                self.tail.next = self.hash[key]
            self.hash[key].prev = self.tail
            self.tail = self.hash[key]
            if self.head is not None:
                first = self.head.key
                self.head = self.hash[first].next
                self.head.prev = None
                del self.hash[first]
            else:
                self.head = self.hash[key]

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










