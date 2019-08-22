# reverse words in a string


# "    " output is wrong lol
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = []

        temp = ""


        for i in s:
          if i == " ":
              if temp != "":
                reverse.append(temp)
                temp = ""
          else:
            temp = temp + i
            
        if temp != "":

            reverse.append(temp)
        
        return " ".join(reverse[::-1])
        
solution = Solution()
print(","+solution.reverseWords("    ")+',')