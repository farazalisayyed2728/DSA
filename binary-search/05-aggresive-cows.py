class Solution:
    
    def fun(self ,stalls, k , guess):
        cow = 1
        pos = stalls[0]
        
        for i in range(1, len(stalls)):
            dist = stalls[i] - pos
            
            if dist >=  guess:
                cow +=1
                pos = stalls[i]
            
                if cow >= k:
                    return True
                
            
        return False
        
    def aggressiveCows(self, arr, k):
        # code here
        
        arr.sort()
        low = 1
        high = arr[- 1] - arr[0]
        res = 0
        
        while low <= high :
            guess = low + (high - low) // 2
            if self.fun ( arr , k , guess):
                res = guess
                low = guess + 1
                
            else:
                high = guess - 1
                
        return res
        