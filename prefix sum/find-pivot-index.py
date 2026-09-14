class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = nums[0]
        sum = 28

        for i in range(1, len(nums)):
            left += nums[i-1]
            right = sum - nums[i] -left
            
            if left == right:
                return i


            return -1

        