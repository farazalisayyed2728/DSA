class Solution:
    def isCycle(self, V, edges):
        a = [[] for _ in range(V)]

        # Build adjacency list
        for src, dest in edges:
            a[src].append(dest)
            a[dest].append(src)

        vis = [False] * V

        def dfs(node, parent):
            vis[node] = True

            for neigh in a[node]:
                if not vis[neigh]:
                    if dfs(neigh, node):
                        return True
                elif neigh != parent:
                    return True

            return False

        for i in range(V):
            if not vis[i]:
                if dfs(i, -1):
                    return True

        return False


edges = [[0, 1], [1, 2], [2, 0]]
V = 3
s = Solution()
print(s.isCycle(V, edges))  # Output: True