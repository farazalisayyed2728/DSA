class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        need = {}
        have = {}
        
        

        for i in range(len(text)):
            have[text[i]] = have.get(text[i] ,0) + 1
            
            need['b'] = 1
            need['a'] = 1
            need['l'] = 2
            need['o'] = 2
            need['n'] = 1

        res = float('inf')


        for i in need:
            c = i
            fneed = need[i]
            fhave = have.get(i , 0)
            times = fhave / fneed

            res = min(res ,times)
        return res


text = "loonbalxballpoon"
sol = Solution()
print(sol.maxNumberOfBalloons(text))