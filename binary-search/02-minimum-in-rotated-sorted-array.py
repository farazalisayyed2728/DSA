class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums) -1
        

        while low < high :
            guess = low + (high - low) // 2

            if nums[guess] > nums[high]:
                low = guess + 1
             
            else:
                high = guess
                
        return nums[low]    # index nahi number retur karna hai isiliye ye likhe 
        
nums = [3,4,5,1,2]
solution = Solution()
print(solution.findMin(nums))  # Output: 1