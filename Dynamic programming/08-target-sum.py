class Solution(object):
    def findTargetSumWays(self, nums, target):

        n = len(nums)
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total + target) % 2 != 0:
            return 0

        s = (total + target) // 2

        dp = [[0] * (s + 1) for _ in range(n + 1)]

        # Base case
        dp[n][0] = 1

        # Tabulation
        for i in range(n - 1, -1, -1):

            for t in range(s + 1):

                if nums[i] > t:
                    dp[i][t] = dp[i + 1][t]

                else:
                    c1 = dp[i + 1][t - nums[i]]
                    c2 = dp[i + 1][t]

                    dp[i][t] = c1 + c2

        return dp[0][s]