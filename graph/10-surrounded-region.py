class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return 

        n = len(board)
        m = len(board[0])

        x = [1, -1 , 0 , 0]
        y = [0 , 0,1, -1]
        
        def valid(i ,j ):
            return 0 <= i < n and 0 <= j < m

        def dfs(i , j):
            board[i][j] = '#'

            for k in range(4):
                row = i + x[k]
                col = j + y[k]

                if valid(row , col) and board[row][col] == 'O':
                    dfs(row , col)

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i , 0)

            if board[i][m-1] == 'O':
                dfs(i , m -1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0 , j)

            if board[n-1][j] == 'O':
                dfs(n-1 , j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] =='#':
                    board[i][j] = 'O'
                    
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution = Solution()
print(solution.solve(board))