class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # left: money left to reach amount
        @cache
        def dp(left):
            # base case: amount reached
            if left == 0: return 0
            if left < 0: return inf
            # recursive steps
            return min(1 + dp(left - c) for c in coins)
        coins = dp(amount) 
        return -1 if isinf(coins) else coins
