# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -inf

        def calc(node):

            if not node: return 0

            left = calc(node.left)
            right = calc(node.right)
            self.max_path = max(self.max_path, max(
                node.val,
                node.val + left,
                node.val + right,
                node.val + left + right
            ))


            return max(node.val, node.val + left, node.val + right)
        
        calc(root)
        return self.max_path