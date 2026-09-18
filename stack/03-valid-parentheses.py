class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        st = []
        

        for i in range(len(s)):
            
            if s[i] == "(":
                st.append(s[i])

                continue

            if s[i] == ")":
                if not st or st[-1] != "(":
                    return False
                st.pop()
                continue
        


            if s[i] == "{":
                st.append(s[i])
                continue 

            if s[i] == "}":
                if not st or st[-1] != "{":
                    return False
                st.pop()   
                continue     
                       
            if s[i] == "[":
                st.append(s[i])
                continue 

            if s[i] == "]" :
                if not st or st[-1] != "[":

                    return False
                st.pop()
                continue

    


        if st:
            return False

        return True



s = "()[]{}"
solution = Solution()
print(solution.isValid(s))