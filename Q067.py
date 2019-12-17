"""
Q067
Add Binary
Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = 0
        carry = 0
        result = ""
        a = a[::-1]
        b = b[::-1]

        if len(a) > len(b):
            a, b = b, a

        while True:

            if i < len(a) and i < len(b):
                if a[i] == "1" and b[i] == "1":
                    if carry == 0:
                        result = "0" + result
                    else:
                        result = "1" + result
                    carry = 1
                elif a[i] == "1" or b[i] == "1":
                    if carry == 0:
                        result = "1" + result
                        carry = 0
                    else:
                        result = "0" + result
                        carry = 1
                else:
                    if carry == 0:
                        result = "0" + result
                    else:
                        result = "1" + result
                    carry = 0

            elif len(a) <= i < len(b):
                if b[i] == "1":
                    if carry == 1:
                        result = "0" + result
                        carry = 1
                    else:
                        result = "1" + result
                        carry = 0
                else:
                    if carry == 1:
                        result = "1" + result
                        carry = 0
                    else:
                        result = "0" + result
                        carry = 0


            else:
                if carry == 1:
                    result = "1" + result
                break

            i += 1


        return result


a = "100"
b = "110010"

sol = Solution()
print(sol.addBinary(a, b))












