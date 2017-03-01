# https://leetcode.com/problems/two-sum/?tab=Description
# COMPLETED

class Solution(object):
    def twoSum(self, nums, target):
        num_hash = {}
        for index, i in enumerate(nums):
            if i in num_hash:
                num_hash[i].append(index)
            else:
                num_hash[i] = [index]
        print(num_hash)
        for index, i in enumerate(nums):
            temp = target-i
            if temp in num_hash:
                if i != temp:
                    return [index, num_hash[temp][-1]]
                elif len(num_hash[temp]) > 1:
                    return [index, num_hash[temp][-1]]
        return None