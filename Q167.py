__author__ = 'linchin'
class Solution1:
    # brute force

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0,len(numbers)):

            comp = target - numbers[i]

            if comp in numbers[i+1:]:

                return [i+1, numbers[i+1:].index(comp)+1+i+1]



class Solution2:
    # from leetcode: double side sliding window
    # very fast


    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers)-1

        while numbers[i] + numbers[j] != target:

            if numbers[i] + numbers[j] > target:

                j -= 1

            else:

                i += 1

        return [i+1, j+1]





sol = Solution2()

print(sol.twoSum([2,7,11,15],9))