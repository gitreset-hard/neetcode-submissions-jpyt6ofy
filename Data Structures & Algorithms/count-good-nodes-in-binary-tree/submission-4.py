# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, _max):

            if not node:
                return
            
            if node.val >= _max:
                _max = node.val
                self.good += 1

            dfs(node.left, _max)
            dfs(node.right, _max)
        
        self.good = 0

        dfs(root, root.val)
        return self.good