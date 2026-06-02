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

            maybe we have to check dfs for every 0 -> n-1 ?
        """
        visited = set()
        def has_cycle(curr_node, parent) -> bool:
            if curr_node in visited:
                return True
            
            visited.add(curr_node)
            for neighbor in graph[curr_node]:
                # as undirected graphs, the nodes are a neighbor of each, so don't want to go to dfs into the parent to avoid looping / false positive
                if neighbor != parent:
                    # current node becomes the parent for it's neighbor 
                    if has_cycle(neighbor, curr_node):
                        return False
            
        if has_cycle(0,-1):
            return False
            
        return len(visited) == n
            

        
