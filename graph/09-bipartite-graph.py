class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        colors = [-1] * n


        def dfs(node , c ):
            colors[node] = c

            for neigh in graph[node]:
                # neigh = graph[node][j]
                if colors[neigh] == -1:
                    if not dfs(neigh , 1 - c ):
                        return False 
                elif colors[neigh] == c:
                    return False

            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i , 0):
                    return False

        return True
