class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [-4,-1,0,3,10]
        i = 1
        j = 1
        n = len(nums)

        while i < j:
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return nums
