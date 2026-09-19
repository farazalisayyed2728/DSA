class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        st = []
        res = []

        for i in range(len(s)):
            c = s[i]

            if not st:
                st.append([c,1])
                continue

            if st[-1][0] != c:
                st.append([c, 1])
                continue

            st[-1][1] += 1

            if st[-1][1] == k :
                st.pop()

        while st:
            p = st.pop()
            
            while p[1] > 0:
                res.append(p[0])
                p[1] -= 1

        res.reverse()

        return "".join(res)

s = "deeedbbcccbdaa"
k = 3
sol = Solution()
print(sol.removeDuplicates(s, k))