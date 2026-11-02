class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        
        n = len(arr)
        
        dp = [[False] * (sum + 1) for _ in range(n + 1)]
        
        
        for i in range(n + 1) :
            dp[i][0] =True
            
        for i in range(n-1 , -1 ,-1):
            
            for target in range(1, sum + 1):
                
                if arr[i] > target:
                    dp[i][target] = dp[i + 1][target]
                    
                else:
                    c1 = dp[i + 1] [target - arr[i]]
                    c2 = dp[i + 1] [target]
                    dp[i][target] = c1 or c2
                    
        return dp[0][sum]
            
arr = [3, 34, 4, 12, 5, 2]
sum = 9
solution = Solution()
print(solution.isSubsetSum(arr , sum)) 