from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        """
            - add edge at a time
            - is there a cycle?
            - the redundant edge is the one that makes it a cycle
                -  could run dfs everytime: unoptimal
                - if both vertices are not in the grpah already, then adding it cant make a cycle
        """

        graph = defaultdict(list)

        def hasCycle(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei != parent:
                    if hasCycle(nei, node):
                        return True
            visited.remove(node)
            
        

        for x,y in edges:
            existed = x in graph and y in graph
            
            graph[x].append(y)
            graph[y].append(x)
                        
            if existed:
                visited = set()
                if hasCycle(x,-1):
                    return [x,y]

        