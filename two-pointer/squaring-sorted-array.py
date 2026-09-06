class Solution(object):
    from typing import List
    def sortedSquares(self, nums:List[int]) -> List [int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        siz = len(nums)
        neg = []
        pos = []
       
       for num in nums:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)


        #case 1
        if len(neg) == 0:
            return [X * X for X in pos]

        #case 2
        if len(pos) == 0:
            res = [X * X for X in neg]
            res.reverse()
            return res

        #case 3
        neg = [X * X for X in neg][::-1] #sq , reverse
        pos = [X * X for X in pos]
        n , m = len(neg), len(pos)
        res = []
        
        i = j = 0

        while i < n and j < m :
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
                
