class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        f = {}
        
        f['2'] = "abc"
        f['3'] = "def"
        f['4'] = "ghi"
        f['5'] = "jkl"
        f['6'] = "mno"
        f['7'] = "pqrs"
        f['8'] = "tuv"
        f['9'] = "wxyz"
        res = []
        def fun(idx , diary):

            if idx == len(digits) :
                res.append("".join(diary))
                return

            #first choice
            
            choice = f[digits[idx]]

            for j in range(len(choice)):
                diary.append(choice[j])

                fun( idx+ 1 , diary )
                diary.pop()

        if digits == "":
            return []


        fun(0 , [])

        return res

