import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        n = len(heights)
        m = len(heights[0])

        res = [[float('inf')] * m for _ in range(n)]

        pq = []
        res[0][0] = 0
        heapq.heappush(pq, (0, (0, 0)))

        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        while pq:
            dist, (row, col) = heapq.heappop(pq)

            if dist > res[row][col]:
                continue

            if row == n - 1 and col == m - 1:
                return dist

            for k in range(4):
                r = row + x[k]
                c = col + y[k]

                if r < 0 or r >= n or c < 0 or c >= m:
                    continue

                absdiff = abs(heights[row][col] - heights[r][c])
                newwt = max(dist, absdiff)

                if newwt < res[r][c]:
                    res[r][c] = newwt
                    heapq.heappush(pq, (newwt, (r, c)))

        return 0
