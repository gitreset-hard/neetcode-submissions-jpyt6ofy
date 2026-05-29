from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
    
        visited = set()
        count = 0

        def dfs(curr_node):
            if curr_node in visited:
                return False

            visited.add(curr_node)

            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        
        for idx in range(n):
            if idx not in visited:
                dfs(idx)
                count += 1
        
        return count