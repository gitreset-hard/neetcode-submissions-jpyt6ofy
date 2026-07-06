# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def delete(node, target):
            if not node: return
            
            if node.val == target:
                # leaf
                if not node.left and not node.right:        
                    return None
                
                # if one child
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                else: # two children
                    # find successor, requires swapping 
                    # can eitehr take the smalles ton the right side or largest on left side.
                    # convention is smallest on right
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    
                    node.val =  curr.val
                    node.right = delete(node.right, curr.val)       
                    return node    


            if key < node.val:
                node.left = delete(node.left,target)
            
            elif key > node.val:
                node.right = delete(node.right, target)
        
            return node

        return delete(root, key)
            
