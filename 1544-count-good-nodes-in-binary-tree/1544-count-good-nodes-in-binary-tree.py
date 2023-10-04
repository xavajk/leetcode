# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # pass down max value seen on path
        # update when necessary
        def dfs(node, max_val):
            # if we are at edge of branch return 0
            if not node:
                return 0
            if node.val >= max_val:
                return 1 + dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))
            else:
                return dfs(node.left, max(max_val, node.val)) + dfs(node.right, max(max_val, node.val))
        
        return dfs(root, root.val)