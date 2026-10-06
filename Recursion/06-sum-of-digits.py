class Solution:
    def sumOfDigits(self, n):
        # code here
        if n == 0:
            return 0
            
        d = n % 10
        
        n = n // 10
        
        ans = self.sumOfDigits(n)
        
        return d + ans  


n = 678
sol = Solution()
print(sol.sumOfDigits(n))