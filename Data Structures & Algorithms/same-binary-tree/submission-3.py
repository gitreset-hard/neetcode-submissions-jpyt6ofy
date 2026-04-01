# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def compare(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False
            
            if n1.val != n2.val:
                return False
            
            return compare(n1.left, n2.left) and compare(n1.right, n2.right)
        
        return compare(p,q)