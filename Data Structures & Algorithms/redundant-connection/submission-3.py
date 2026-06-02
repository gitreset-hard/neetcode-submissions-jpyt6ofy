from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            - undirected
            - nodes: 1 -> n
            - start: acyclic, and n-1 edges
            - problem:  add an edge to make a cycle
            - goal: find edge to make ayclic, if many, return the last edge in input that makes it cyclic

            # one approach: inefficient
                - add node / edge one at a time from edges
                - every iteration, perform dfs, to find when a cycle is made
        """
        graph = defaultdict(list)
        
        def has_cycle(curr, parent):
            if curr in curr_path:
                return True
            curr_path.add(curr)

            for neighbor in graph[curr]:
                if neighbor != parent:
                    if has_cycle(neighbor, curr):
                        return True
            
            return False

        for edge in edges:
            x,y = edge
            graph[x].append(y)
            graph[y].append(x)

            # now for each elemet in graph, do cycle detection
            for n in range(max(graph)+1):
                curr_path = set() # cycle detection
                if has_cycle(n, -1):
                    return edge
