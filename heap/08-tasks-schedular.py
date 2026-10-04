class Solution(object):
    def leastInterval(self, tasks, n):
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())

        count_max = 0
        for f in freq.values():
            if f == max_freq:
                count_max += 1

        # Number of slots created by the most frequent task
        result = (max_freq - 1) * (n + 1) + count_max

        # We cannot have fewer intervals than the number of tasks
        return max(len(tasks), result)



    #     class Solution(object):
    # def leastInterval(self, tasks, n):
    #     import heapq

    #     freq = {}
    #     free = {}

    #     for task in tasks:
    #         freq[task] = freq.get(task, 0) + 1
    #         free[task] = 1

    #     pq = []

    #     for key, value in freq.items():
    #         heapq.heappush(pq, (-value, key))

    #     seat = 1

    #     while pq:
    #         pulled = []

    #         while pq:
    #             fr, child = heapq.heappop(pq)
    #             fr = -fr

    #             if free[child] <= seat:
    #                 if fr > 1:
    #                     heapq.heappush(pq, (-(fr - 1), child))
    #                     free[child] = seat + n + 1
    #                 break
    #             else:
    #                 pulled.append((fr, child))

    #         for fr, child in pulled:
    #             heapq.heappush(pq, (-fr, child))

    #         seat += 1

    #     return seat - 1

