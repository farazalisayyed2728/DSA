class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_end = nums[0]
        min_end = nums[0]
        res = abs(nums[0])

        for i in range(1,len(nums)):
            v1 = max_end + nums[i]
            v2 = nums[i]
            

            max_end = max(v1,v2)
            
            v3 = min_end + nums[i]
            min_end = min(v3, v2)
            
            res = max(res, abs(max_end), abs(min_end))
        return res