# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if path to current node is less than nodes value, cut off from parent
        # at each node, choose max of left, right, and left + right
        # node: current node, path: sum of path to current node
        res = [root.val]
        def recur(node):
            # at end of branch
            if not node:
                return 0
            # recursive steps
            left_path = max(recur(node.left), 0)
            right_path = max(recur(node.right), 0)
            res[0] = max(res[0], left_path + node.val + right_path)
            return node.val + max(left_path, right_path)
        recur(root)
        return res[0]