import functools
import operator

class Solution1(object):
    # exceed time limit

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(0,len(nums)):

            if nums[i] not in nums[0:i] + nums[i+1:]:

                return nums[i]


class Solution2(object):


    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        before = []
        after = [i for i in nums]
        print(after)

        after.remove(nums[0])
        print(after)

        for i in nums:

            if (i not in before) and (i not in after):

                return i
            else:
                before.append(i)
                if i in after:
                    after.remove(i)


class Solution3(object):

    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        return 2*sum(set(nums)) - sum(nums)


# different solutions from leetcode
# what do these mean?

def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key

class Solution(object):

    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
            print((num,res))

        return res


def singleNumber3(self, nums):
    return 2 * sum(set(nums)) - sum(nums)


def singleNumber4(self, nums):
    return functools.reduce(lambda x, y: x ^ y, nums)


def singleNumber(self, nums):
    return functools.reduce(operator.xor, nums)


sol = Solution()

a = [2,2,1,1,5,5,6,7,7,8,8]
print(sol.singleNumber(a))





