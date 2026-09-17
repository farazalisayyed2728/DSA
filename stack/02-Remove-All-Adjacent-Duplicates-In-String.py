class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.fun(s)
    def fun(self , s):
        n = len(s)
        st = []
        res = ""

        for i in range(len(s)):
            if not st:
                st.append(s[i])
                continue

            if st[-1] == s[i]:
                st.pop()
                continue

            st.append(s[i])

        while st:
            res += st.pop()

        return res[::-1]
        