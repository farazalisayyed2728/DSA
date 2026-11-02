class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:

        n = len(val)

        dp = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            for cap in range(W + 1):

                if wt[i] > cap:
                    dp[i][cap] = dp[i + 1][cap]

                else:
                    yes = val[i] + dp[i + 1][cap - wt[i]]
                    no = dp[i + 1][cap]

                    dp[i][cap] = max(yes, no)

        return dp[0][W]

val = [1, 2, 3]
wt = [4, 5, 1]
W = 4
solution = Solution()
print(solution.knapsack(W ,val , wt))