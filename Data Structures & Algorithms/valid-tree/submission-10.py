from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            valid undirected graph:
                - no disconnected nodes
                - no cycles
        """
        # check: disconnected graph AND for cycle
        if n - 1 != len(edges):
            return False

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        """ assumption: in a valid tree, should be able to reach all the nodes
                        from a single search rather multi point 
                        tha'ts why we can start at 0

            we also checked for cycles at the start, so just need to see if we can reach all nodes
        """
        visited = set()
        def dfs(curr_node) -> bool:
           
            visited.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)
        return len(visited) == n
            

        
