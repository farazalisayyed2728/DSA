class Solution:
    
    def dfs(self , adj):
        V = len(adj)
        vis = [False] * V
        res = []
        
        def dfsTrav(node): 
            
            vis[node] = True
            res.append(node)
            
            for neigh in adj[node] :
    
                if not vis[neigh]:
                    dfsTrav(neigh)
                    
                
                
        dfsTrav(0)
        return res