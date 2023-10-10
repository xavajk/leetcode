class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(i, j):
            if i not in range(m) or j not in range(n) or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # change all areas connected to edge to temp value 'T'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in [0, m - 1] or j in [0, n - 1]):
                    dfs(i, j)

        # change all remaining '0's to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # change un-surrounded regions back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'