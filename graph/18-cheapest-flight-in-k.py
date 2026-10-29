class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        
        INF = 10**8
        res =  [INF] * n
        res[src] = 0

        for _ in range( k + 1):
            temp = res[:]  # for copy of prev distance

            for s , d , wt in flights:

                if res[s] != INF and temp[d] > res[s] + wt:
                    temp[d] = res[s] + wt

            
            res = temp

        return res[dst]   if res[dst] != INF else -1

