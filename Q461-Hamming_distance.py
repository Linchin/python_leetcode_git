__author__ = 'linchin'



class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        '''
        Return the Hamming distance between equal-length sequences
        '''

        sx = '{0:031b}'.format(x)
        sy = '{0:031b}'.format(y)

#        sx = format(x, "08b")
#        sy = format(y, "08b")

#        print(sx)

#        print(sy)

        count = 0
        for i in range(0,31):
            count = count + (sx[i] != sy[i])

        return count


x = 1232
y = 12412

s = Solution()

distance = s.hammingDistance(x, y)
print(distance)