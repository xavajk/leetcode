# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # maintain heap of size k
        # return heap[k - 1]
        heap = []
        # inorder dfs traversal to preserve value order
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            heapq.heappush(heap, node.val)
            dfs(node.right)
            return

        dfs(root)
        for i in range(k - 1):
            heapq.heappop(heap)
        # while len(heap) > k:
        #     heap.pop()
        return heap[0]