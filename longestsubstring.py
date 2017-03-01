# https://leetcode.com/problems/longest-palindromic-substring/?tab=Description
# COMPLETED

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def recurse(arr, start, end, total, index_set, main_arr):
            if start < 0:
                main_arr[index_set] = total
                return
            elif end > len(arr)-1:
                main_arr[index_set] = total
                return
            if arr[start] == arr[end]:
                total += 1
                recurse(arr, start-1, end+1, total, index_set, main_arr)
            else:
                main_arr[index_set] = total 
        
        break_arr = [0]*(len(s)*2 + 1)
        for index, i in enumerate(break_arr):
            if index % 2 == 1:
                break_arr[index] = s[int(index/2)]
        
        count_arr = [0] * len(break_arr)
        for index, i in enumerate(break_arr):
            recurse(break_arr, index-1, index+1, 0, index, count_arr)
        
        
        arg_max = [0, None]
        for index, i in enumerate(count_arr):
            if i > arg_max[0]:
                arg_max[0] = i
                arg_max[1] = index
        
        real_index = int(arg_max[1]/2)
        print(real_index)
        
        if break_arr[arg_max[1]] != 0:
            start = real_index - int(arg_max[0]/2)
            end = real_index + int(arg_max[0]/2)
            temp_arr = s[start:end+1]
        
        else:
            real_index -=1
            start = real_index - int(arg_max[0]/2)+1
            end = real_index + int(arg_max[0]/2)
            temp_arr = s[start:end+1]
        
        s_n = ''
        for index, i in enumerate(temp_arr):
            if i != 0:
                s_n += i
        return s_n