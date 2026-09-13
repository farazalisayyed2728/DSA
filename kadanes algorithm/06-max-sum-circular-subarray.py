class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cong = nums[0]
        bjp = nums[0]
        max_sum = nums[0]
        min_sum = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]

            v1 = cong + nums[i]
            v2 = nums[i]

            cong = max(v1, v2)
            bjp = min(bjp + nums[i], nums[i])

            max_sum = max(max_sum, cong)
            min_sum = min(min_sum, bjp)

        if max_sum < 0:
            return max_sum

        circular_sum = total - min_sum

        return max(max_sum, circular_sum)