class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        siz = len(nums)
        left = 0
        right =0

        for i in range(nums):
            sum = [nums[i]] ,[nums[j]] ,[nums[k]] == 0

            if sum < target:
                left += 1

                elif sum > target:
                    right +=1

                    else:
                        


