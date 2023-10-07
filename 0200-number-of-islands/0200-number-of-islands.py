class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])
        
        # DFS Implementation
        # def dfs(i, j):
        #     # base case: out of bounds or at '0'
        #     if i not in range(m) or j not in range(n):
        #         return
        #     if grid[i][j] == '0' or (i, j) in seen:
        #         return 
        #     seen.add((i, j))
        #     # recurse in all directions
        #     dfs(i + 1, j)
        #     dfs(i - 1, j)
        #     dfs(i, j + 1)
        #     dfs(i, j - 1)

        # BFS Implementation (more suited to finding islands)
        def bfs(i, j):
            queue = deque()
            seen.add((i, j))
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()
                dirs = [ (r + dr, c + dc) for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]] ]
                for i, j in dirs:
                    if i in range(m) and j in range(n) and grid[i][j] == '1' and (i, j) not in seen:
                        queue.append((i, j))
                        seen.add((i, j))

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    bfs(i, j)
                    islands += 1
                    # dfs(i, j)
        return islands