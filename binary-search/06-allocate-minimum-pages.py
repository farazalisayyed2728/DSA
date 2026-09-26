class Solution:
    
    def fun (self, arr, limit, stud):
        k = 1
        page = arr[0]
        
        for i in range(1, len(arr)):
            
            if page + arr[i] <= limit :
                page += arr[i]
                
            else:
                k +=1
                page = arr[i]
                
                if k > stud:
                    return False
                    
        return True
        
    def findPages(self, arr, k):
        # code here
        n = len(arr)        
        
        
        if len(arr) < k:
            return -1
            
            
            
        low = max(arr)
        high = sum(arr)
        
        res = -1
        
        while low <= high:
            guess = low + (high -low) // 2
            
            if self.fun(arr, guess , k):
                res = guess
                high = guess -1
                
            else:
                low = guess + 1
                
        return res
                
            
arr= [12, 34, 67, 90]
k = 2
solution = Solution()
print(solution.findPages(arr, k))  