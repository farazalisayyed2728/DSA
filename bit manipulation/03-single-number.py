class Solution(object):
    def singleNumber(self, nums):
        
        x = 0
        for i in range(len(nums)):
            x = x ^ nums[i]

        return x

nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums))