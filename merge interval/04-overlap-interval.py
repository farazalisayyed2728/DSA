class Solution:
    def isIntersect(self, intervals):
       # Code Here
        intervals.sort()
           
        start1 = intervals[0][0]
        end1 = intervals[0][1]
           
        for i in range(len(intervals)):
               
            start2 = intervals[i][0]
            end2 = intervals[i][1]
               
            if end1 >= start2:
                return True
                    
                    
            start1 = start1
            end1 = max(end1, end2)
    
        return False

intervals = [[1, 3], [5, 7], [2, 4], [6, 8]]
solution = Solution()
print(solution.isIntersect(intervals))  # Output: True