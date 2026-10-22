class Solution:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        a = [[] for _ in range(V)]
        
        for src , dest in edges:
            a[src].append(dest)
            
            
        vis = [False] * V
        path = [False] * V
        
        
        def dfs(node):
            vis[node] = True
            path[node] = True
            
            for neigh in a[node]:

                if path[neigh]:
                    return True
                    
                if not vis[neigh]:
                    if dfs(neigh):
                        return True
                    
                    
                    
            path[node] = False
            return False
            
        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
        return False
                    