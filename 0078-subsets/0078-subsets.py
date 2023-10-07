class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [[]], set()
        n = len(nums)
        def backtrack(i):
            if i == n:
                return
            # dont take
            backtrack(i + 1)
            # take
            subset.add(nums[i])
            res.append(sorted(list(subset)))
            backtrack(i + 1)
            subset.remove(nums[i])
        backtrack(0)
        return res