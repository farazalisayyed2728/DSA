class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        
        n = len(val)
        
        dp = [[-1] * (W + 1) for _ in range(n)]
        
        
        # code here
        def fun(i , cap):
            
            if i == n:
                return 0
                
            if dp[i][cap] != -1:
                return dp[i][cap]
                
            if wt[i] > cap :
                
                dp[i][cap] = fun(i + 1 , cap )
                return dp[i][cap]
                
                
            yes = val[i] + fun(i + 1 , cap-wt[i])
            no = fun(i + 1 , cap)
            
            dp[i][cap] = max(yes , no)
            
            return dp[i][cap]
            
        return fun(0 , W)

val = [1, 2, 3]
wt = [4, 5, 1]
W = 4
solution = Solution()
print(solution.knapsack(W ,val , wt))