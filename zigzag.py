# https://leetcode.com/problems/zigzag-conversion/?tab=Description
# COMPLETED

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 0:
            return None

        final_str = [[] for x in range(numRows)]
        move_counter = 0
        counter = 0
        state = 0
        while counter < len(s):
            final_str[move_counter].append(s[counter])

            # Going Down
            if state == 0:
                if move_counter+1 >= numRows:
                    move_counter -= 1
                    state = 1
                else:
                    move_counter += 1

            # Going Up
            elif state == 1:
                if move_counter <= 0:
                    move_counter += 1
                    state = 0
                else:
                    move_counter -= 1

            counter += 1

        result = ''
        for i in final_str:
            result = result + ''.join(i)
        return result

driver = Solution()

test_data = ("paypalishiring", 1)
print("Test Data:", test_data)
print("Results:", driver.convert(test_data[0], test_data[1]))   