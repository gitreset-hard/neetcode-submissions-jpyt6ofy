from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
            - undirected
            - n: num nodes 
            - every cycle increases # of edges. cycle is irrelevant, just need to traverse

            # approach
                - do a dfs from each node (if not already seen)
                - num of traversals == ans 
                    - if we see all the nodes (n) in one go then 1 graph
        """


        adj = defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set() # global
        graph_count = 0

        def dfs(curr_node):
            # base case
            if curr_node in visited:
                return False
            visited.add(curr_node)

            for neighbor in adj[curr_node]:                
                if neighbor not in visited:
                    dfs(neighbor)

        
        for num in range(n):
            if num not in visited:
                dfs(num)
                graph_count += 1
        
        return graph_count
