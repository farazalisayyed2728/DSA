class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k -1
        sum = 0
        
        for i in range(k):
            sum = sum + arr[i]
            if i <= high:
                i += 1

                
       
            