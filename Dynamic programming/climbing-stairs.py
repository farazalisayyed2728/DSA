class Solution(object):
    def rob(self, nums):

        n = len(nums)
        dp = [[-1] * 2 for _ in range(n)]

        def fun(nums, n, i, free):

            if i == n:
                return 0

            if dp[i][free] != -1:
                return dp[i][free]

            if free == 0:
                dp[i][free] = fun(nums, n, i + 1, 1)
                return dp[i][free]

            c1 = nums[i] + fun(nums, n, i + 1, 0)
            c2 = fun(nums, n, i + 1, 1)

            dp[i][free] = max(c1, c2)

            return dp[i][free]

        return fun(nums, n, 0, 1)

nums =  [1,2,3,1]
solution = Solution()
print(solution.nums())