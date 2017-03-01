# https://leetcode.com/problems/string-to-integer-atoi/?tab=Description
# NOT COMPLETED


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        valid_numerals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        if len(str) == 0:
            return 0

        neg_flag = 0
        start = 0
        zero_flag = 0
        total = ''

        if str[0] == '-':
            if len(str) == 1:
                return 0
            neg_flag = 1
            start = 1

        elif str[0] == '+':
            if len(str) == 1:
                return 0
            start = 1

        for i in range(start, len(str)):
            if str[i] == ' ':
                continue
            elif str[i] in valid_numerals:
                if str[i] != '0':
                    zero_flag = 1
                    total = total + str[i]
                else:
                    if zero_flag != 0:
                        total = total + str[i]

        if neg_flag == 0:
            return int(total)
        else:
            return -int(total)



driver = Solution()

test_data = ("3221")
print("Test Data:", test_data)
print("Results:", driver.myAtoi(test_data))