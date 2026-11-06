class Solution(object):
    def singleNumber(self, nums):
        
        x = 0
        for i in range(len(nums)):
            x = x ^ nums[i]

        return x