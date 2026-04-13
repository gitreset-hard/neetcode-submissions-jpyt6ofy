# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, _min, _max):
            if not node:
                return True
            
            if not (_min < node.val < _max):
                return False
            
            return dfs(node.left, _min, node.val) and dfs(node.right, node.val, _max)
        
        
        return dfs(root, -inf, inf)
        
            