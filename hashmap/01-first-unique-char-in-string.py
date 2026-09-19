class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        f = {}

        for i in range(len(s)):
            f[s[i]] = f.get(s[i], 0) + 1


        for i in range (len(s)):

            if f[s[i]] == 1:
                return i

        return -1

s = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(s))