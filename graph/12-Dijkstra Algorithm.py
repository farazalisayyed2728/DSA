import heapq

class Solution:
    def dijkstra(self, adj: list[list[list[int]]], src: int) -> list[int]:
        n = len(adj)
        pq = []
        dist = [float('inf')] * n

        dist[src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for neigh, wt in adj[node]:
                if d + wt < dist[neigh]:
                    dist[neigh] = d + wt
                    heapq.heappush(pq, (d + wt, neigh))

        return dist