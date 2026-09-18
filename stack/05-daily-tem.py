class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st =[]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            

            while st and  temperatures[st[-1]] <  temperatures[i]:
                old = st.pop()
                res[old] = i - old      
            st.append( i)

                
        return res 

temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))
