from collections import deque
class Solution:
    def bfs(self, adj):
        # code here
        n = len(adj)
        vis = [False] * n
        res = []
        
        q = deque()
        q.append(0)
        vis[0] = True
        
        while q:
            node = q.popleft()
            res.append(node)
            
            for neigh in adj[node]:

                if not vis[neigh] :
                    vis[neigh] = True
                    q.append(neigh)
                    
        return res