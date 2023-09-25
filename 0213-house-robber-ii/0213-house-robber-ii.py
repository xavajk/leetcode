class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, robbed, first): # i: current house
            # base case: at last house
            if i >= n: return 0
            if i == n - 1: return nums[i] if not robbed and not first else 0
            # recursive steps
            if i == 0: return max(nums[i] + dp(i + 1, True, True), dp(i + 1, False, False))
            if not robbed: return max(nums[i] + dp(i + 1, True, first), dp(i + 1, False, first))
            return dp(i + 1, False, first)
        return dp(0, False, False)