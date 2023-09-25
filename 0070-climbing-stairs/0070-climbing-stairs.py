class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
        # i: steps left to the end
            # base case(s): reach the top of the stairs - i == n
            #               already at the top of the stairs - i > n
            if i == n: return 1
            if i > n: return 0
            # recursive steps
            ways = dp(i + 1) + dp(i + 2)
            return ways
        return dp(0)