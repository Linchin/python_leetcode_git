"""
Q017
Letter Combinations of a Phone Number
Medium

String; Backtracking.

Given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""

        output = []

        projection = {"2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"}

        def generate(i, result):
            if i == len(digits):
                output.append(result)
            else:
                for item in projection[digits[i]]:
                    generate(i+1, result+item)

        generate(0, "")

        return output



sol = Solution()
a = "23"
print(sol.letterCombinations(a))




