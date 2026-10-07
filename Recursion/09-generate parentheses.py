class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def fun(open , close , temp):

            if open == n and close == n :
                res.append(''.join(temp))
                return 

            if open < n :
                temp.append('(')
                fun(open + 1 , close , temp)
                temp.pop()


            if close < open :
                temp.append(')')
                fun(open , close + 1 , temp)
                temp.pop()

        fun(0, 0, []) 

        return res


n = 3
sol = Solution()
print(sol.generateParenthesis(n)) 

