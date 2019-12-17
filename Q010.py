"""
Q010
Regular Expression Matching
Hard

string; DP; backtracking.

Given an input string (s) and a pattern (p), implement
regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the ENTIRE input string (not partial).

Note:
1. s could be empty and contains only lowercase letters a-z.
2. p could be empty and contains only lowercase letters a-z,
    and characters like . or *.

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".
"""

from collections import defaultdict

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if not p:
            if not s:
                return True
            return False

        P = len(p)

        j = 0

        p_par = []
        current = []

        # pre-process p into partitions
        while j < P:
            if "a" <= p[j] <= "z":
                current.append(p[j])
            elif p[j] == ".":
                if current:
                    p_par.append(current)
                p_par.append(["."])
                current = []
            elif p[j] == "*":
                if current:
                    temp = current.pop()
                    if current:
                        p_par.append(current)
                else:
                    temp = p_par[-1].pop()
                    if not p_par[-1]:
                        p_par.pop()
                p_par.append([temp, "*"])
                current = []
            j += 1
            continue

        if current:
            p_par.append(current)

#        print(p_par)

        # find whether the correct partition for s exists
        # recursive

        equal_map = defaultdict(list)

        def equal(s, p):
            # return True if s is equal to p (partition) per regex rules

            # avoid the matching process again
            if p in equal_map[s]:
                return True

            if len(p) == 1:
                if len(s) == 1:
                    if p[0] == "." or p[0] == s:
                        equal_map[s].append(p)
                        return True
                return False

            if len(p) == 2:
                if p[0] == "." and p[1] == "*":
                    equal_map[s].append(p)
                    return True
                elif p[1] == "*":
                    if not s:
                        equal_map[s].append(p)
                        return True
                    for item in s:
                        if item != p[0]:
                            return False
                    equal_map[s].append(p)
                    return True

            if len(s) != len(p):
                return False

            # for i_e in range(len(s)):
            #     if s[i_e] != p[i_e]:
            #         return False

            if s == "".join(p):
                equal_map[s].append(p)
                return True
            return False

        def find_next_partition(s, p_par):
            # recursion
            # find the partition in s that matches p_par[0]
            if len(p_par) == 1:
                if equal(s, p_par[0]):
                    return True
                return False
            for ii in range(0, len(s)+1):
                if equal(s[:ii], p_par[0]):
                    if find_next_partition(s[ii:], p_par[1:]):
                        return True


        if find_next_partition(s, p_par):
            return True

        return False


sol = Solution()
s = "aab"
p = "aac"
print(sol.isMatch(s, p))












