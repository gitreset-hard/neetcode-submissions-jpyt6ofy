# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            in order traversal gives sorted list
            so kth smallest is from the start, if k = 1 then first node.
        """
        self.count = k
        self.ans = 0

        def dfs(node):
            if not node: return 0

            dfs(node.left)
            self.count -= 1
            if self.count == 0:
                self.ans = node.val
            dfs(node.right)
        
        dfs(root)
        return self.ans