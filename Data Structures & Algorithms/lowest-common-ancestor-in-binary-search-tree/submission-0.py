# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                print(1, curr.val, p.val, q.val)
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                print(2, curr.val, p.val, q.val)
                curr = curr.left
            else:
                print(3, curr.val, p.val, q.val)
                return curr