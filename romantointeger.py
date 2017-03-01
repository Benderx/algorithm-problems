# https://leetcode.com/problems/roman-to-integer/?tab=Description
# COMPLETED

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        running = 0
        flag = False
        d = {"I": 1, "V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        for index in range(0, len(s)-1):
            if flag == True:
                flag = False
                continue
            if d[s[index]] >= d[s[index+1]]:
                running += d[s[index]]
            else:
                running += d[s[index+1]] - d[s[index]]
                flag = True
        
        if flag == False:
            running += d[s[-1]]
        
        return running