# https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
# IN PROGRESS


class Solution(object):
    def find_first_char(self, to_find, string):
        for i in range(len(string)):
            if to_find == string[i]:
                return i

    def lengthOfLongestSubstring(self, s):
        highest = []
        track = []
        s_list = list(s)
        # print(s_list)
        
        for index, i in enumerate(s_list):
            if i not in track:
                track.append(i)
                if len(track) > len(highest):
                    highest = []
                    for j in track:
                        highest.append(j)
            else:
                track.append(i)
                # print('old', track)
                repeated_index = self.find_first_char(i, track)
                new_track = []
                for j in range(repeated_index+1, len(track)):
                    new_track.append(track[j])
                track = new_track
                # print('new:', track)

        # print(highest)
        # highest_str = ''
        # for i in highest:
        #     highest_str = highest_str + i
        # return highest_str
        return len(highest)


s = Solution()
t0 = 'aab'
t1 = 'abcabcbb'  # abc
t2 = 'bbbbb'     # b
t3 = 'pwwkew'    # wke
t4 = 'pwetywuiw' # etywui
t5 = 'bbtablud'  # tablud

print(s.lengthOfLongestSubstring(t0))
print(s.lengthOfLongestSubstring(t1))
print(s.lengthOfLongestSubstring(t2))
print(s.lengthOfLongestSubstring(t3))
print(s.lengthOfLongestSubstring(t4))
print(s.lengthOfLongestSubstring(t5))