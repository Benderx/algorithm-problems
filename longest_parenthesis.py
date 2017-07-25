# //https://leetcode.com/problems/longest-valid-parentheses/#/description
# IN PROGRESS

class Solution(object):
    def check_longest(self, longest, start, finish):
        if finish - start > longest[0]:
            longest[1] = start
            longest[2] = finish
            longest[0] = finish - start
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0

        lefts = 0
        start = 0
        finish = 0
        
        longest = [0, 0, 0]

        for i in s:
            if i == '(':
                lefts += 1
                finish += 1
            elif lefts != 0 and i == ')':
                lefts -= 1
                finish += 1
            else:
                # print(s[start:finish])
                self.check_longest(longest, start, finish)
                finish += 1
                start = finish

        flag = 0
        while s[start] == ')' or lefts != 0:
            while s[start] == ')':
                lefts += 1
                start += 1
                if start == len(s) - 1:
                    flag = 1
                    break
                # print(s[start:finish], lefts)
            if flag == 1:
                break
            while s[start] == '(' and lefts != 0:
                lefts -= 1
                start += 1
                if start == len(s) - 1:
                    flag = 1
                    break
                # print(s[start:finish], lefts)
            if flag == 1:
                break
        self.check_longest(longest, start, finish)

        # return s[longest[1]:longest[2]]
        return longest[0]



s = Solution()
test0 = '(()'
test1 = ')()())'
test2 = '()()'
test3 = '(()))(((())))'
test4 = '()(()'
# print(test0, ':', s.longestValidParentheses(test0))
# print(test1, ':', s.longestValidParentheses(test1))
# print(test2, ':', s.longestValidParentheses(test2))
# print(test3, ':', s.longestValidParentheses(test3))
print(test4, ':', s.longestValidParentheses(test4))