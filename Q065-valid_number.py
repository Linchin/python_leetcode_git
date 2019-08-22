__author__ = 'linchin'



class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            b = float(s)
            return True
        except ValueError:
            return False



a = '  1 a    '

s = Solution()
b = s.isNumber(a)
print(b)