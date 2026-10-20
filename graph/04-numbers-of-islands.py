class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        x = [-1,1,0,0]
        y = [0,0,-1,1]

        vis = [[False] * m for _ in range(n)]

        def valid(i , j , n , m):
            return 0 <= i < n and 0 <= j < m

        def DFS(i , j):
            vis[i][j] = True

            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if (valid(row, col, n, m)
                    and grid[row][col] == '1'
                    and not vis[row][col]):
                    DFS(row, col)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not vis[i][j]:
                    DFS(i,j)
                    count += 1

        return count 



