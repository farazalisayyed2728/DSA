class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        res = 0

        for num in nums:
            if num % 2 == 0:
                res |= num

        return res