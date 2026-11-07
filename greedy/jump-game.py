class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        reach = 0 
        for i in range(len(nums)):
            if reach < i :
                return False

            reach = max(reach , i + nums[i])

            if reach >= n - 1 :
                return True 

        return True 
    