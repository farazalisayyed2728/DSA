class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        dp = [[-1] * 2  for _ in range(n)]

        def fun(i, buy):

            if i == n :
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy == 1:
                c1 = fun(i + 1, 0) - prices[i]
                c2 = fun(i + 1, 1)

            else:
                c1 = fun(i + 1, 1) + prices[i]
                c2 = fun(i + 1, 0)

            dp[i][buy] = max(c1 , c2)

            return dp[i][buy]

        return fun(0, 1)


prices = [7 ,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))