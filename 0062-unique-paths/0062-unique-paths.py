class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # robot can only move down (i - 1) or right (j + 1)
        @cache
        def dp(i, j): # i, j: position on grid
            # base cases: out of bounds or at goal
            if i == m - 1 and j == n - 1: return 1
            if i >= m or j >= n: return 0
            # recursive steps: move down and right
            return dp(i + 1, j) + dp(i, j + 1)
        return dp(0, 0)