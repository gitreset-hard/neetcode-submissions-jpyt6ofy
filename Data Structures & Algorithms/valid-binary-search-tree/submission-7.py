# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')
        def dfs(node, _min, _max):
            if not node:
                return True
            
            if node.val <= _min or node.val >= _max:
                return False
            
            return dfs(node.left, _min, node.val) and dfs(node.right, node.val, _max)
        

        return dfs(root, -INF, INF)