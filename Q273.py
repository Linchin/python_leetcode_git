"""
Q273
Integer to English Words
Hard

Convert a non-negative integer to its english words
representation. Given input is guaranteed to be less than 231 - 1.
"""


class Solution:
    def numberToWords(self, num: int) -> str:

        if not num:
            return "Zero"

        def num2str(number):

            word1 = ""

            flag = 0

            if number // 100:
                word1 += word[number//100] + " Hundred"
                flag = 1
            number %= 100
            if number // 10 == 1:
                if flag:
                    word1 += " "
                word1 += word[number]
                return word1
            elif number // 10 > 1:
                if flag:
                    word1 += " "
                word1 += word[number//10 * 10]
                number %= 10
                if number:
                    word1 += " " + word[number]
                return word1
            if number:
                if flag:
                    word1 += " "
                word1 += word[number]
            return word1

        final_str = ""
        word = {1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen",
                20: "Twenty",
                30: "Thirty",
                40: "Forty",
                50: "Fifty",
                60: "Sixty",
                70: "Seventy",
                80: "Eighty",
                90: "Ninety"}

        cc = {0: " Billion",
              1: " Million",
              2: " Thousand",
              3: ""}

        t = [0 for i in range(0, 4)]

        t[0] = num // 1000000000
        t[1] = (num % 1000000000) // 1000000
        t[2] = (num % 1000000) // 1000
        t[3] = num % 1000

        flag = 0

        for i in range(0, 4):
            if t[i] > 0:
                if flag:
                    final_str += " "
                final_str += num2str(t[i]) + cc[i]
                flag = 1

        return final_str

a = 1000
sol = Solution()
print(sol.numberToWords(a))





