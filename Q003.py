__author__ = 'linchin'


class Solution:

    # 9.84%
    def lengthOfLongestSubstring_old(self, s):
        """
        :type s: str
        :rtype: int
        """

        opt = 0

        length = len(s)

        if length == 0:
            return 0

        if length == 1:
            return 1

        j = 0

        for i in range(0,length):


            for j in range(i, length+1):

                if j == length or s[j] in s[i:j]:

                    break


            if j-i > opt:

                opt = j-i

        return opt

    def lengthOfLongestSubstring(self, s):

        # shifting window method
        """
        :type s: str
        :rtype: int
        """

        num, maxnum, ss = 0,0,''

        for each in s:

            if each in ss:

                ss = ss.split(each)[-1]+each

                num = len(ss)

            else:

                ss += each
                num += 1
                maxnum = max(maxnum, num)

        return maxnum










result = Solution()
print(result.lengthOfLongestSubstring(s="pwwkew"))
