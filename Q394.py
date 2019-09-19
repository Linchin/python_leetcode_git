"""
Q394
Decode String
Medium

Stack; DFS.

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
 inside the square brackets is being repeated exactly k times.
 Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra
white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not
contain any digits and that digits are only for those repeat
numbers, k. For example, there won't be input like 3a or 2[4].
"""


class Solution:
    def decodeString(self, s: str) -> str:

        result = ""
        i = 0

        def rep_func(i):

            rep = int(s[i])
            rep_str = ""

            i += 1

            # read the value of repetition
            while "0" <= s[i] <= "9":
                rep = rep*10 + int(s[i])
                i += 1

            # read the string to be repeated
            i += 1
            while 1:
                if "1" <= s[i] <= "9":
                    # recursion if there's embedded reps
                    temp, i = rep_func(i)
                    rep_str += temp
                elif "a" <= s[i] <= "z" or "A" <= s[i] <= "Z":
                    rep_str += s[i]
                    i += 1
                else:
                    i += 1
                    return rep_str * rep, i


        while i < len(s):
            if "a"<=s[i]<="z" or "A"<=s[i]<="Z":
                result += s[i]
                i += 1
            else:
                result0, i = rep_func(i)
                result += result0

        return result

sol = Solution()
a = "30[avd]"
print(sol.decodeString(a))








