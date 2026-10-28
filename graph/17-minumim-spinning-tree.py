import heapq
class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        a = [[] for _ in range(V)]
        
        for s, d , wt in edges:
            a[s].append((d , wt))
            a[d].append((s , wt))

                
        pq = []
        vis = [0] * V
        total = 0
        
        heapq.heappush(pq, (0, 0))
         
        while pq:
             weight, node = heapq.heappop(pq)
             
             if vis[node] == 1:
                 continue
             
             vis[node] = 1
             
             total += weight

             for neigh , wt in a[node]:
                 if vis[neigh] == 0:
                     heapq.heappush(pq,(wt ,neigh))
                     
                     
        return total