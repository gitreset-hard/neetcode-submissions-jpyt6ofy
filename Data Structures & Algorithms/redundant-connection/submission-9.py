from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        idea: 
            - can only have a cycle when adding an edge where the two nodes already existed
                - if the graph was already connected, 
                - if was disconnected, then adding an edge can connect 
        """
        
        graph = defaultdict(list)
        def has_cycle(curr, parent):
            if curr in visited:
                return True
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor != parent:
                    if has_cycle(neighbor, curr):
                        return True
            return False


        for idx, edge in enumerate(edges):
            x,y = edge
            existed = x in graph and y in graph
            graph[x].append(y)
            graph[y].append(x)

            if existed:
                visited = set()
                if has_cycle(x, -1):
                    return edge
                




