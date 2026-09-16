class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        b = []
        res = []

        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            if start1 <= start2:
                
                if end1 >= start2:
                    s = max(start1, start2)
                    e = min(end1, end2)
                    res.append([s,e])

            else:
                if end2 >= start1:
                    s = max(start1,start2)
                    e = min(end1 ,end2)
                    res.append([s ,e])

            if end1 <= end2 :
                i += 1
            else:
                j += 1

        return res

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
solution = Solution()
print(solution.intervalIntersection(firstList, secondList))