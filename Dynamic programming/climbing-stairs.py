class Solution(object):
    def climbStairs(self, n):
        dp = {}

        def solve(i):
            if i == n:
                return 1

            if i > n :
                return 0

            if i in dp :
                return dp[i]

            a1 = solve(i + 1 )
            a2 = solve(i + 2 )

            dp[i] = a1 + a2


            return dp[i]
        
        return solve(0)

        
n = 2
solution = Solution()
print(solution.climbStairs(n))