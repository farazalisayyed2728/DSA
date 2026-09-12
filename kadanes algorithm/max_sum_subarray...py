class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        best_end = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            v1 = best_end + nums[i]
            v2 = nums[i]
            i += 1
            best_end = max(v1, v2)
            ans = max(ans , best_end)

        return ans