class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs in all directions:
        #   - can only move downhill (< heights[i])
        #   - left and up returns true for pacific ocean
        #   - right and down returns true for atlantic ocean
        #   - if both pacific and atlantic are true, add to result
        m, n = len(heights), len(heights[0])
        def dfs(i, j, val, seen):
            # base case: current height is greater than previous
            if i in range(m) and j in range(n) and heights[i][j] > val:
                return ''
            # at edge of pacific ocean border
            if i == -1 or j == -1:
                return 'P'
            # at edge of atlantic ocean border
            if i == m or j == n:
                return 'A'
            # look in every direction
            val = heights[i][j]
            seen.add((i, j))
            dirs = [ (i + di, j + dj) for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]] ]
            paths = ""
            for i, j in dirs:
                if (i, j) not in seen:
                    paths += dfs(i, j, val, seen)
            return paths

        # check if each cell can reach both oceans
        # res = []
        # for i in range(m):
        #     for j in range(n):
        #         paths = dfs(i, j, heights[i][j], set())
        #         if 'P' in paths and 'A' in paths:
        #             res.append([i, j])
        # return res

        # NEETCODE SOLUTION
        pac, atl = set(), set()
        def ndfs(i, j, val, seen):
            if i < 0 or i == m or j < 0 or j == n or heights[i][j] < val or (i, j) in seen:
                return
            seen.add((i, j))
            ndfs(i + 1, j, heights[i][j], seen)
            ndfs(i - 1, j, heights[i][j], seen)
            ndfs(i, j + 1, heights[i][j], seen)
            ndfs(i, j - 1, heights[i][j], seen)

        for i in range(m):
            ndfs(i, 0, heights[i][0], pac)
            ndfs(i, n - 1, heights[i][n - 1], atl)
        for j in range(n):
            ndfs(0, j, heights[0][j], pac)
            ndfs(m - 1, j, heights[m - 1][j], atl)

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res