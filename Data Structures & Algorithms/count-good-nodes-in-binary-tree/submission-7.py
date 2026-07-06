# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.count = 0 

        def dfs(node, curMax):
            if not node: return

            if node.val >= curMax:
                self.count += 1
            
            dfs(node.left, max(node.val, curMax))
            dfs(node.right, max(node.val, curMax))
        
        dfs(root, float('-inf'))
        return self.count
            

        
        