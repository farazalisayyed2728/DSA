class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        res = []
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        


intervals = [[1,3],[6,9]]
solution = Solution()
print(solution.insert(intervals, [2,5]))