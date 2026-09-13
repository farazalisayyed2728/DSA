class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minend = nums[0]
        maxend = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = minend * nums[i]
            v3 = maxend * nums[i]
            

            maxend = max(v1,v2,v3)
            minend = min(v1,v2,v3)

         
            res = max(res,maxend)
            
        return res