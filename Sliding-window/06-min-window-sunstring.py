class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not s or not t: 
            return ""

        need = {} 
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        window ={}

        low = 0
        high = 0

        have = 0
        need_count = len(need) 
        
        res_len = float('inf')
        start = 0
        
        while high < len(s):
            ch = s[high]
            window [ch] = window.get(ch, 0) +1
            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                window_size = high - low + 1
                if window_size < res_len:
                    res_len = window_size
                    start = low

            
                left_ch = s[low]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                low += 1
            high +=1
            
        if res_len == float('inf'):
            return ""
            res = min(res, high - low)

        return s[start:start + res_len]



s = "ADOBECODEBANC"
solution = Solution()
result = solution.minWindow(s, "ABC")
print(result)
