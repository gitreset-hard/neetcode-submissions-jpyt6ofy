# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,_min,_max):
            if not node:
                return True
            
            if node.val <= _min or node.val >= _max:
                return False
            
            return check(node.left, _min, node.val) and check(node.right, node.val, _max)
        
        return check(root, -inf, inf)