class Solution:
    def maxSubarraySum(self, arr, k):

        n = len(arr)
        sum = 0

        for i in range(k):
            sum += arr[i]
            i += 1

            res = sum
            low = 0
            high = k -1

        while high < n -1:
            sum -= arr[low]
            low += 1
            high += 1
        
        
            sum += arr[high]

            res = max(res,sum)
        return res



arr = [100,200,300,400 ]
obj = Solution()
result = obj.maxSubarraySum(arr, 2)
print(result)


       
            