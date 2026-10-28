import heapq
class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        m = len(grid[0])

        res = [[float('inf')] * m for _ in range(n)]

        pq = []
        res[0][0] = grid[0][0]
        heapq.heappush(pq, (grid[0][0], (0, 0)))

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

                newwt = max(dist, grid[r][c])

                if newwt < res[r][c]:
                    res[r][c] = newwt
                    heapq.heappush(pq, (newwt, (r, c)))

        return -1

grid = [[0,2], [1,3]]
solution = Solution()
print(solution.swimInWater(grid))