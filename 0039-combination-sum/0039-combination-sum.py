class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        def backtrack(i, left):
            # base cases: i out of bounds or reached target
            if left == 0:
                res.append(combo.copy())
                return 
            if i >= len(candidates) or left < 0:
                return
            # if amount left is greater than or equal to candidates[i]
            # take or dont take
            if left >= candidates[i]:
                # take
                combo.append(candidates[i])
                backtrack(i, left - candidates[i])
                # dont take
                combo.pop()
                backtrack(i + 1, left)
            # else, move on to next number if available
            else:
                backtrack(i + 1, left)
        backtrack(0, target)
        return res