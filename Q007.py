class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # overflow case

        if abs(x) > 2 ** 31 - 1:
            return 0

        # treat the minus sign

        flag = 0

        if x < 0:
            x = -x
            flag = 1


        # remove all the 0s at the end of the number

        while x % 10 == 0 and x > 0:
            x = x // 10

        x_str = str(x)

        y = 0


        # reverse the number


        for i in x_str[::-1]:

            y = y * 10 + int(i)

        if flag == 1:
            y = -y

        if abs(y) > 2 ** 31 - 1:
            return 0

        return y






solution = Solution()

print(solution.reverse(1534236469))