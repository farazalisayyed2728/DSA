class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        res = []

        start1 =  newInterval[0]
        end1 =  newInterval[1]

        insert = False

        for i in range(len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]
            

            if end2 < start1:
                res.append(intervals[i])
                # start1 = start1
                # end1  = max(end1 , end2)
                continue
            
            if start2 > end1:
                if insert == False:
                    res.append([start1, end1])
                    insert = True

                res.append(intervals[i])
                continue

            
            start1 = min(start1,start2)
            end1 = max(end1 ,end2)


        if insert == False:
            res.append([start1 ,end1])

        return res



intervals = [[1,3],[6,9]]
solution = Solution()
print(solution.insert(intervals, [2,5]))