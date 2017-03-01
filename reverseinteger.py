# https://leetcode.com/problems/reverse-integer/?tab=Description
# COMPLETED

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = ''
        flag = False
        for i in str(x):
            if i == "-":
                flag = True
                continue
            s += i
        
        if flag == True:
            s += "-"
        lol = int(s[::-1])
        if lol > 2147483647 or lol < -2147483647:
            return 0
        return lol