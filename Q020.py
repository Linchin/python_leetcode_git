"""
Q020

Valid Parenthesis

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        value = {"(":-1, ")":1, "{":-2, "}":2, "[":-3, "]":3}

        for item in s:

            if value[item] < 0:

                stack.append(value[item])

                continue

            elif len(stack) > 0 and stack.pop() + value[item] == 0:

                continue

            else:
                return False

        if sum(stack) >= 0:
            return True
        else:
            return False

sol = Solution()

a = "["

print(sol.isValid(a))