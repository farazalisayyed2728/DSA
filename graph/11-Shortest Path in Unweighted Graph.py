from collections import deque

from django.db.migrations import graph

class Solution:
    def shortestPath(self, V, edges, src, dest):
        a = [[] for _ in range(V)]

        # Build adjacency list
        for s, d in edges:
            a[s].append(d)
            a[d].append(s)

        res = [-1] * V
        vis = [False] * V

        q = deque()
        q.append((src, 0))
        vis[src] = True

        while q:
            node, dis = q.popleft()

            res[node] = dis

            # Destination reached
            if node == dest:
                return dis

            for neigh in a[node]:
                if not vis[neigh]:
                    vis[neigh] = True
                    q.append((neigh, dis + 1))

        return -1

edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3], [3, 4]]
V = 5
src = 0
dest = 8
solution = Solution()
print(solution.shortestPath(V, edges, src, dest))