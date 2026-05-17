# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.good = 0

        def dfs(node, _max):
            if not node:
                return 0
            
            if node.val >= _max:
                self.good += 1
            
            _max = max(_max, node.val)

            dfs(node.left, _max)
            dfs(node.right, _max)
        
        dfs(root, root.val)
        # dfs(root.right, root.val)
    
        return self.good