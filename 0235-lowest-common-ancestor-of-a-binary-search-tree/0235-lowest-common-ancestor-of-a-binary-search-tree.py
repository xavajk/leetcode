# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, path, target):
            # base cases
            if not node:
                return []
            if node == target:
                path.append(node)
                return path
            path.append(node)
            if node.val > target.val:
                dfs(node.left, path, target)
            else:
                dfs(node.right, path, target)
            return path

        ppath = dfs(root, [], p)
        qpath = dfs(root, [], q)
        i, last = 0, None
        for i in range(min(len(ppath), len(qpath))):
            if ppath[i] == qpath[i]:
                last = ppath[i]
        return last