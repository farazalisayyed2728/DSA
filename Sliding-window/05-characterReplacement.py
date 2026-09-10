class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low = 0
        high = 0
        res = 0
        f = {} #hashmap


        while high < len(s):
            f[s[high]] = f.get(s[high], 0)+1
            high += 1


            len_s = high - low
            max_int = max(f.values())
            diff = len_s - max_int

            while diff > k:
                f[s[low]] -=1
                low +=1

                max_int = max(f.values())
                len_s = high - low
                diff = len_s - max_int

            len_s = high - low
            res = max(res,len_s)

        return res

s = "ABAB"
obj = Solution()
result = obj.characterReplacement(s, 2)

print(result)