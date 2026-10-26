class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        for u , v , w in times:
            graph[u].append((v , w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0 , k)]

        while pq :
            d , node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for neigh , wt in graph[node]:
                new_dist = d + wt

                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    heapq.heappush(pq, (new_dist , neigh))

        ans = max(dist[1:])
        return ans if ans != float('inf') else -1
