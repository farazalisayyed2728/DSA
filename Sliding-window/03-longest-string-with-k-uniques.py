class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        low = 0
        high = 0
        
        f = {}
        res = -1
        
        while high < len(s) :
            
            f[s[high]] = f.get (s[high] ,0) + 1
            high += 1
            
            while len(f) > k:
                f[s[low]] -= 1
            
             
                if f[s[low]] == 0:
                    del f[s[low]]
                    
                low += 1
                
            if len(f) == k :
                arr_len = high - low
                res = max(res, arr_len )
                
        return res