from collections import deque
class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Code here
        a = [[] for _ in range(V)]
        # vector <int> indeg(n,0);
        indeg = [0] * V
        
        for src , dest in edges:
            a[src].append(dest)
            indeg[dest] += 1
            
        q = deque()
        
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
                
        res = []
        
        while q :
            
            node = q.popleft()
            res.append(node)
            
            for neigh in a[node]:
                indeg[neigh] -= 1
                
                if indeg[neigh] == 0:
                    q.append(neigh)
        return res
            