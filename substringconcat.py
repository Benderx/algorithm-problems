# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?tab=Description
# INCOMPLETE

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return [0]

        len_words = len(words[0])

        words_first_hash = {}
        for i in words:
            if i not in words_first_hash:
                words_first_hash[i] = True

        words_transformed = []
        for key in words_first_hash:
            words_transformed.append(key)

        words_hash = {}
        for index, i in enumerate(words):
            if i not in words_hash:
                words_hash[i] = [words_transformed.index(i), 1]
            else:
                words_hash[i][1] += 1

        print(words_hash)

        # Creae esc strings
        esc_strings = [[] for x in range(len_words)]
        for i in range(len_words):
            x = i
            while x < (len(s) - len_words):
                if s[x:x+len_words] in words_hash:
                    esc_strings[i].append((words_hash[s[x:x+len_words]][0], x))
                else:
                    esc_strings[i].append((-1, x))
                x += len_words
        

        num_hash = []
        concats_found = []

        for i in range(len_words):
            # print("esc_string", esc_strings[i])

            num_found_counter = 0
            for k in range(len(words_hash)):
                find_hash[k] = 0

            for index in range(len(esc_strings[i])-(len(words)-1)):
                for inner_index in range(len(words)):
                    x = esc_strings[i][index + inner_index]
                    if x[0] == -1:
                        for k in range(len(words_hash)):
                            find_hash[k] = 0
                    else:
                        if num_hash[x[0]] == 0:
                            num_hash[x[0]] = x[1] + 1
                        else:
                            for k in range(len(words_hash)):
                                find_hash[k] = 0

                            num_hash[x[0]] = x[1] + 1

                    if num_found_counter == len(words):
                        least = [0, num_hash[0]]
                        for o in range(1, len(num_hash)):
                            if num_hash[o] < least[1]:
                                least[1] = num_hash[o]
                                least[0] = o
                        concats_found.append(least[1]-1)
                        # print("FOUND IN", esc_strings[i], "BEGINING WITH", least[1]-1)

        return concats_found






driver = Solution()

test_data = ("wordgoodgoodgoodbestword", ["word","good","best","good"])
print("Test Data:", test_data)
print("Results:", driver.findSubstring(test_data[0], test_data[1]))