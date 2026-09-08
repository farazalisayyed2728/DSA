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
        while high < len(arr):
            sum = sum -arr[low -1]
            if high == len(arr):
                break
            res = max(res,sum)
            low += 1
            high += 1
            
            sum = sum + arr[high]
            
        return res


       
            