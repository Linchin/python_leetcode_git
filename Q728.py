"""
Q728
Self Dividing Numbers
Easy

:math:

A self-dividing number is a number that is divisible by every
digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0,
128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit
zero.

Given a lower and upper number bound, output a list of every possible
self dividing number, including the bounds if possible.
"""

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        self_divide = []

        for i in range(left, right+1):
            text = str(i)
            flag = True
            for item in text:
                if item == "0" or i % int(item) != 0:
                    flag = False
                    break
            if flag:
                self_divide.append(i)

        return self_divide

sol = Solution()
print(sol.selfDividingNumbers(1,22))


