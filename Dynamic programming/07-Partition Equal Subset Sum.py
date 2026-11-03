class Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        
        for i in range(n + 1) :
            dp[i][0] =True
            
        for i in range(n-1 , -1 ,-1):
            
            for t in range(1, target + 1):
                
                if nums[i] > t:
                    dp[i][t] = dp[i + 1][t]
                    
                else:
                    c1 = dp[i + 1] [t - nums[i]]
                    c2 = dp[i + 1] [t]
                    dp[i][t] = c1 or c2
                    
        return dp[0][target]


nums = [1,5,11,5]
solution = Solution()
print(solution.canPartition(nums))