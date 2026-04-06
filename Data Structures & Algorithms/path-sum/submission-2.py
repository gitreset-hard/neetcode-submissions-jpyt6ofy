# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.hasPath = False

        def dfs(node, curSum):
            if not node:
                return 
            
            if not node.left and not node.right:
                if (curSum + node.val) == targetSum:
                    self.hasPath = True

            dfs(node.left, curSum + node.val)
            dfs(node.right, curSum + node.val)
            
            # curSum -= node.val
        
        dfs(root, 0)
        
        return self.hasPath