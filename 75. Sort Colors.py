# 75. Sort Colors
# Python
# Time: 21ms
# Memory: 13.3MB
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero,one,two = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
        for i in range(len(nums)):
            if zero:
                nums[i] = 0
                zero -= 1
            elif one:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2