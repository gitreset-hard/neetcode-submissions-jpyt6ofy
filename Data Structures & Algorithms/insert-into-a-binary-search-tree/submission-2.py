# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        BST is already sorted
        if can insert at the bottom ?
        """
        if not root: return TreeNode(val)

        curr = root
        while curr:

            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
        
        return root