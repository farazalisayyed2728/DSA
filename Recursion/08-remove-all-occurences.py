class Solution:
    def removeCharacter(self, s, c):

        ans = []

        def check(i):
            if i == len(s):
                return

            if s[i] != c:
                ans.append(s[i])

            check(i + 1)

        check(0)

        return ''.join(ans)

s = "geeksforgeeks"
c = 'e'
sol = Solution()
print(sol.removeCharacter(s, c))

