class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1,1,2]
        k= 0
        i = 1
        cm = 1 
        n = len(nums)
        while (cm < n):
            if (nums[cm] == nums[cm -1]):
                cm +=1
                continue
            
            if(nums[k] == nums[cm]):
                k+=1
                cm+=1

            return k

        
            
        
