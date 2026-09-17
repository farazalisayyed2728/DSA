class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        n = len(start)
        
        start.sort()
        end.sort()
        
        room = 0
        res = 0
        
        i = 0
        j = 0
        
        while i < n and j < n:
            if start[i] < end[j]:
                room +=1
                res = max(res ,room)
                i += 1
                
            else:
                room -= 1
                j +=1
        return res
