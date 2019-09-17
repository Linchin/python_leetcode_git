"""
Q380
Insert Delete GetRandom O(1)
Medium

Array; Hash Table; Design.

Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.
2. remove(val): Removes an item val from the set if present.
3. getRandom: Returns a random element from current set of elements.
    Each element must have the same probability of being returned.

Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()
"""

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_struc = []
        self.data_ind = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data_ind:
            return False

        self.data_struc.append(val)
        self.data_ind[val] = len(self.data_struc) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data_ind:

            index = self.data_ind[val]
            last = self.data_struc[-1]

            self.data_struc[index] = last
            # the order of the following two lines is very important

            # line 1
            self.data_ind[last] = index

            # line 2
            del self.data_ind[val]
            self.data_struc.pop()

            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.data_struc) == 0:
            return None
        rand = random.randint(0, len(self.data_struc)-1)
        return self.data_struc[rand]


randomSet = RandomizedSet()
print(randomSet.insert(1))
print(randomSet.insert(1))
print(randomSet.remove(2))
print(randomSet.insert(2))
print(randomSet.getRandom())
print(randomSet.getRandom())





