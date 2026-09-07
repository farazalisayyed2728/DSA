class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0 
        mid = 0
        high = len(nums) -1

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[low] , nums[i] = nums[i] ,nums[low]
                low += 1
                
            elif nums[i] == 1:
                
                mid += 1
            
            elif nums[i] == 2:
                nums[i] , nums[high] = nums[high] ,nums[i]
                high -= 1
                
            # elif mid < high:
            #     nums[3] , nums[4] = nums[4] ,nums[3]
            #     mid += 1

            while mid < high:
                nums[3] , nums[4] = nums[4] ,nums[3]

        return nums