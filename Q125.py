__author__ = 'linchin'

class Solution1:
    # 140 ms
    # 5% lol

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        i = 0
        j = len(s)-1

        while s[i].isalnum() == False and i < len(s)-1:
            i += 1
        while s[j].isalnum() == False and j > 0:
            j -= 1


        if i >= j:
            return True

        while i < j:

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1


            while s[i].isalnum() == False:
                i += 1
            while s[j].isalnum() == False:
                j -= 1

        return True

Sol = Solution()
print(Sol.isPalindrome("race a car"))








