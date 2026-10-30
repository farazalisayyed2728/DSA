class Solution(object):
    def fib(self, n):
        dp = {}

        def solve(n):
            if n == 0 or n == 1:
                return n

            if n in dp:
                return dp[n]

            a1 = solve(n-1)
            a2 = solve(n-2) 

            dp[n] = a1 + a2

            return dp[n]
            
        return solve(n)