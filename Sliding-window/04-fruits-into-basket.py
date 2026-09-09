class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        low = 0
        high = 0
        f ={}
        res = -1

        while high < len(fruits):
            f[fruits[high]] = f.get(fruits[high] , 0) + 1
            high += 1

            while len(f) > 2:
                f[fruits[low]] -=1

                if f[fruits[low]] == 0:
                    del f[fruits[low]]  

                low +=1
                
            fruits_len = high - low
            res = max(res , fruits_len)

        return res


fruits = [0,1,2,2,3,3,4,4,5,5]
obj = Solution()
result = obj.totalFruit(fruits)
print(result)