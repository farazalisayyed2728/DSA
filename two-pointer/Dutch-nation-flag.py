class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0 
        mid = 0
        high = len(nums) -1

        while mid <= high:
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid] ,nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                
                mid += 1
            
            else:
                nums[mid] , nums[high] = nums[high] ,nums[mid]
                high -= 1
                
        

        return nums




nums = [2, 0, 2, 1, 1, 0]

# Object create
obj = Solution()

# Function call
result = obj.sortColors(nums)

# Output
print(result)