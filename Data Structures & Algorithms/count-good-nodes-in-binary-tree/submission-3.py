# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        self.good = 1

        def dfs(node, path):
            if not node:
                return 
            
            if node.val >= max(path) if path else 0:
                self.good += 1
            
            path.append(node.val)

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
            return
        
        dfs(root, [])
        return self.good