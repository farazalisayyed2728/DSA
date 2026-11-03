class Solution(object):
    def lengthOfLIS(self, nums):

        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1 , -2 , -1):

                c1 = 0
                c2 = 0

                if prev == -1 or nums[i] > nums[prev]:
                    c1 = 1 + dp[i + 1][i + 1]

                c2 =  dp[i + 1][prev + 1]

                dp[i][prev + 1] = max(c1 , c2)

        return dp[0][0]
                
        
nums = [10,9,2,5,3,7,101,18]
solution = Solution()
print(solution.lengthOfLIS(nums))