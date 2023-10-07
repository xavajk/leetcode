class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            # base case: out of bounds or at '0'
            if i not in range(m) or j not in range(n):
                return
            if grid[i][j] == '0' or (i, j) in seen:
                return 
            seen.add((i, j))
            # recurse in all directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    islands += 1
                    dfs(i, j)
        return islands