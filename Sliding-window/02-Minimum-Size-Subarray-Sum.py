class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        res = float('inf')
        low = 0
        high = 0
        sum = 0

        while high < len(nums):
            sum += nums[high]

            while sum >= target:

                window_size = high - low + 1
                res = min(res, high - low + 1)

                sum -= nums[low]
                low += 1

            high += 1
        if res == float('inf'):
            return 0

        return res