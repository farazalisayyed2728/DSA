class Solution(object):
    def leastInterval(self, tasks, n):
        import heapq

        freq = {}
        free = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            free[task] = 1

        pq = []

        for key, value in freq.items():
            heapq.heappush(pq, (-value, key))

        seat = 1

        while pq:
            pulled = []
            found = False

            while pq:
                fr, child = heapq.heappop(pq)
                fr = -fr

                if free[child] <= seat:
                    if fr > 1:
                        heapq.heappush(pq, (-(fr - 1), child))
                    free[child] = seat + n + 1
                    found = True
                    break

                else:
                    pulled.append((fr, child))

            for fr, child in pulled:
                heapq.heappush(pq, (-fr, child))
            if found:
                seat += 1
            else:
                seat = min(free[task] for _, task in pq)
        return seat - 1

