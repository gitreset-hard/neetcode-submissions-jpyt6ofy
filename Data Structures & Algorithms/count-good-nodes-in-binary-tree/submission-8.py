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

        def dfs(node, _max):
            if not node: return 0

            dfs(node.left, max(_max, node.val))
            dfs(node.right, max(_max, node.val))

            if node.val >= _max:
                self.count += 1
            
        dfs(root, root.val)
        return self.count
