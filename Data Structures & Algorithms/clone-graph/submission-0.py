"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        seen = dict()

        def dfs(curr_node):
            if not curr_node:
                return
            
            if curr_node in seen:
                return seen[curr_node]
            
            # clone curr_node
            curr_clone = Node(curr_node.val)
            seen[curr_node] = curr_clone

            for neighbor in curr_node.neighbors:
                curr_clone.neighbors.append(dfs(neighbor))
            
            return curr_clone
        
        return dfs(node)

