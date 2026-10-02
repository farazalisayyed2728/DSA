class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        import heapq
        n = len(profits)
        proj = []
        

        for i in range(n):
            proj.append([capital[i], profits[i]])


        proj.sort()

        hq = []
        idx = 0

        while k > 0:
            while idx < n and proj[idx][0] <= w:
                heapq.heappush(hq ,- proj[idx][1])
                idx +=1

            if not hq :
                return w

            w -= heapq.heappop(hq)
            k -= 1

        return w

