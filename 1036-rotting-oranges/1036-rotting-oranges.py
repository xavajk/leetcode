class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # add each rotted orange at time = 0 to queue
        # bfs for each rotted orange updating grid values per iteration
        # increase time for each bfs iteration
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        time = 0
        while fresh > 0 and queue:
            qlen = len(queue)
            for k in range(qlen):
                i, j = queue.popleft()
                dirs = [ (i + di, j + dj) for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]] ]
                for i, j in dirs:
                    if i in range(m) and j in range(n) and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        queue.append((i, j))
            time += 1
        
        return time if fresh == 0 else -1