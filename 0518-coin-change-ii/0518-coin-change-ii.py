class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(total=amount, coin=0): # coin: current coin index, left: amount left
            # base cases: reached amount or gone over
            if total == 0: return 1
            if total < 0: return 0
            if coin == len(coins): return 0
            # recursive steps: add ways of taking and not taking current coin
            return dp(total - coins[coin], coin) + dp(total, coin + 1)
        return dp()
