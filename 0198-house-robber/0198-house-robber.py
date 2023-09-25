class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, robbed): # i: current house
            # base case: at last house
            if i == n - 1: return nums[i] if not robbed else 0
            if i >= n: return 0
            # recursive steps
            if not robbed: return max(nums[i] + dp(i + 1, True), dp(i + 1, False))
            else: return dp(i + 1, False)
        return dp(0, False)