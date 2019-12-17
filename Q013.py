"""
Q013
Roman to Integer
Easy

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        total = 0

        for i in range(0, len(s)-1):
            if dic[s[i+1]] > dic[s[i]]:
                total -= dic[s[i]]
            else:
                total += dic[s[i]]
        total += dic[s[-1]]
        return total


a = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(a))







