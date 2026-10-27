class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
         INF = 10**8
         res =[INF] * V
         res[src] = 0
         
         
         for _ in range(V -1) :
             
             for s , d , wt in edges:
                 
                 if res[s] != INF and res[d] > res[s] + wt:
                     res[d] = res[s] + wt
                     
         for s , d , wt in edges:
    
             
             if res[s] != INF and res[d] > res[s] + wt:
                 return [-1]
                 
         return res