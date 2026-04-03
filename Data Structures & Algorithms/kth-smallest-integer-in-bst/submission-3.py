# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        BST means left < parent < right
        we want left to right, so left first is inOrder traversal      
        """

        self.traversal = []
        self.count = 0

        def dfs(node):

            if not node: return

            dfs(node.left)
            self.traversal.append(node.val)
            self.count += 1
            dfs(node.right)
        
        dfs(root)
        return self.traversal[k-1]
        



        