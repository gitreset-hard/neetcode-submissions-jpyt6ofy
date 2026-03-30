# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        self.good = 0 # root node
        # TODO: 1 or 0?

        def dfs(node, _max):
            if not node: return

            if node.val >= _max:
                self.good += 1
            
            _max = max(_max, node.val)

            dfs(node.left, _max)
            dfs(node.right, _max)

            return
        
        dfs(root, root.val)

        return self.good


            

