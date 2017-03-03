# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?tab=Description
# INCOMPLETE

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """


driver = Solution()

test_data = ("barfoothefoobarman", ["foo", "bar"])
print("Test Data:", test_data)
print("Results:", driver.findSubstring(test_data[0], test_data[1]))