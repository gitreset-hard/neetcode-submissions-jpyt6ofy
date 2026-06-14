from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        def dfs(curr):
            visited.add(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    dfs(nei)
        
        connections = 0
        visited = set() # global
        for i in range(n):
            if i not in visited:
                dfs(i)
                connections += 1
        
        return connections