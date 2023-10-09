class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # maintain set of visited cells
        seen = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            # base cases: out of bounds; already seen; a '0'
            if i not in range(m) or j not in range(n):
                return 0
            if grid[i][j] == 0 or (i, j) in seen:
                return 0
            # move in all directions and sum total counts of 1 for island
            seen.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = max(res, dfs(i, j))
        return res