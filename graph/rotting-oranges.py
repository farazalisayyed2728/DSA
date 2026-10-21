from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = [-1, 1 , 0 , 0]
        y = [ 0 , 0 , -1, 1]
        n = len(grid)
        m = len(grid[0])

        def valid(i , j , n , m):
            return 0 <= i < n and 0 <= j  < m 

        q = deque()
        fresh = 0
        time = 0

        for i in range(len(grid)):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i , j])
                    grid[i][j] = -2

                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            time += 1
            s = len(q)

            while s > 0:
                s -= 1
                p = q[0]
                q.popleft()
                r = p[0]
                c = p[1]
                for k in range(4):
                    row = r + x [k]
                    col = c + y [k]

                    if valid(row , col ,n,m) and grid[row][col] == 1:
                        q.append([row , col])
                        grid[row][col] = -2
                        fresh -=1

        if fresh > 0:
            return -1

        return time 

grid = [[2,1,1],[1,1,0],[0,1,1]]
s = Solution()
print(s.orangesRotting(grid))