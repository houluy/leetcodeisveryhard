# My solution
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indx, x in enumerate(nums):
            for indy, y in enumerate(nums[indx + 1:]):
                if (x + y) == target:
                    return [indx, indy + indx + 1]

# Learning from official solutions
# One-pass Hash Table
# Trade space for time
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for indx, x in enumerate(nums):
            if target - x in dic:
                return [dic.get(target - x), indx]
            else:
                dic[target - x] = indx
