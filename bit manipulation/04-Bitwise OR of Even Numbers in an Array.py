class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        res = 0

        for num in nums:
            if num % 2 == 0:
                res |= num

        return res

nums = [1,2,3,4,5,6]
s = Solution()
print(s.evenNumberBitwiseORs(nums))