class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1,1,2]
        k= 1
        cm = 1 
        n = len(nums)
        while cm < n:
            if (nums[cm] != nums[cm -1]):
                nums[k] = nums[cm]  
                k += 1

            cm+=1

            return k

        
            
        
