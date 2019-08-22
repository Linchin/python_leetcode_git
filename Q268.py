class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)   
        
        array_sum = sum(nums)
        
        return (n+1)*n/2 - array_sum
        