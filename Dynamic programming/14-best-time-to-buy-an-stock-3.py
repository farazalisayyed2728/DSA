class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        k = 2
        dp = [[[-1]* 2 for _ in range(k + 1)] for _ in range(n)]

        def fun(i, k, buy):

            if i == n or k == 0:
                return 0

            if dp[i][k][buy] != -1:
                return dp[i][k][buy]

            if buy == 1:
                c1 = fun(i + 1, k , 0) - prices[i]
                c2 = fun(i + 1, k, 1)

            else:
                c1 = fun(i + 1, k - 1, 1) + prices[i]
                c2 = fun(i + 1, k, 0)

            dp[i][k][buy] = max(c1 , c2)

            return dp[i][k][buy]

        return fun(0, k, 1)