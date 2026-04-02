# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        out = []
        q = [root]

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.pop(0)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                level.append(curr.val)

            out.append( level)

        return out
