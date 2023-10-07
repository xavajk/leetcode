class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res, perm = [], []
        # def backtrack(i, seen):
        #     # if we have a complete permuation
        #     if len(perm) == len(nums):
        #         res.append(perm.copy())
        #         return
        #     # out of bounds
        #     if i == len(nums):
        #         return
        #     # for each number not seen in nums
        #     # either take or dont take
        #     for n in nums:
        #         if n in seen: 
        #             continue
        #         # take
        #         perm.append(n)
        #         seen.add(n)
        #         backtrack(i + 1, seen)
        #         # dont take
        #         perm.pop()
        #         seen.remove(n)
        #         backtrack(i + 1, seen)
        # backtrack(0, set())
        # return res

        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res