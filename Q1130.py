"""
Q1130
Minimum cost tree from leaf values
Medium

Given an array arr of positive integers, consider all binary
trees such that:

- Each node has either 0 or 2 children;
- The values of arr correspond to the values of each leaf
    in an in-order traversal of the tree.  (Recall that a node
    is a leaf if and only if it has 0 children.)
- The value of each non-leaf node is equal to the product of the
    largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest
possible sum of the values of each non-leaf node.  It is
guaranteed this sum fits into a 32-bit integer.


"""
from typing import List
from functools import lru_cache

class Solution_dp:

    def mctFromLeafValues(self, arr: List[int]) -> int:

        memo = {}

        def dp(start, end):
            # starting and ending index of the current tree

            if (start, end) in memo:
                return memo[start, end]

            # end of iteration
            if end == start + 1:
                memo[start, end] = (arr[start]*arr[end], max(arr[start], arr[end]))
                return memo[start, end]
            elif end == start:
                memo[start, end] = (0, arr[start])
                return 0, arr[start]

            sum = float('inf')
            for i in range(start+1, end+1):
                # i is the starting index of the right tree
                left = dp(start, i-1)
                right = dp(i, end)
                this_sum = left[0] + right[0] + left[1] * right[1]
                if this_sum < sum:
                    sum = this_sum

            max_val = max(arr[start:end+1])
            memo[start, end] = (sum, max_val)

            return sum, max_val

        return dp(0, len(arr)-1)[0]


sol1 = Solution_dp()
arr = [6,2,4]
print(sol1.mctFromLeafValues(arr))


class Solution_greedy:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        res = 0

        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)

        return res

sol2 = Solution_greedy()
arr = [6,2,4]
print(sol2.mctFromLeafValues(arr))







#
#
# class Solution_stack:
#     def mctFromLeafValues(self, arr: List[int]) -> int:

