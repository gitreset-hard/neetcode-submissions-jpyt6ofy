# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            k = 1 : 2 1 3 -> 1 2 3 -> 1
            k = 4 : 4 3 5 2 -> 2 3 4 5 -> 5

            brute force: collect all nums, sort and give kth smallest
        """

        if not root: return []
        self.traversal = []

        def dfs(node):
            if not node: return 

            dfs(node.left)
            self.traversal.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return self.traversal[k-1] 