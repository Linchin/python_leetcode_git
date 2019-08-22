class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        result = []

        flag = 0

        temp = digits[-1]

        if temp < 9:

            result = digits
            result[-1] = result[-1] + 1

        else:

            result = [0]

            flag = 1

            for i in digits[0:-1][::-1]:

                if i < 9 and flag == 1:
                    flag = 0
                    result = [i+1] + result

                elif i < 9 and flag == 0:
                    result = [i] + result

                elif i == 9 and flag == 1:
                    flag = 1
                    result = [0] + result

                else:
                    flag = 0
                    result = [i] + result

            if flag == 1:
                result = [1] + result

        return result

sol = Solution()

print(sol.plusOne([0]))





