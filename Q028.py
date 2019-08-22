class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        flag = 0
        
        if needle == "":
        	return 0

        else:
        	for i in range(0,len(haystack)-len(needle)+1):

        		j = 0

        		while haystack[i+j] == needle[j]:
        			j += 1

        			if j == len(needle):

        				flag = 1

        				break

        		if flag  == 1:
        			break



		if flag == 1:
			return i
		else:
			return -1
