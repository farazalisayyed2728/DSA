class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = {}
        for i in range(len(s)):
            f[s[i]] = f.get(s[i], 0) + 1

        odd = False
        res = 0

        for i in f:
            val = f[i]

            if val %2 == 0:
                res += val

            else:
                res += val -1
                odd = True


        if odd:
            return res + 1


        return 

s = "abccccdd"
sol = Solution()
print(sol.longestPalindrome(s))