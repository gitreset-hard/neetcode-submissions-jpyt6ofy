from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        valid if:
            - no cycles
                given it's an undirected graph:
                    - at any step, we can look back and see the parent but that's not a valid cycle
            - not disconnected  (?)

            0 : [1]
            1: [0, 2, 3, 4]
            2: [3, 1]
            3: [1,2]
            4: [1]

        """
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set() # global

        def has_cycle(edge, parent):
            if edge in visited:
                return True

            visited.add(edge)

            for neighbor in graph[edge]:

                if neighbor not in visited or neighbor != parent:
                    if has_cycle(neighbor, edge):
                        return True

            
            return False
        
        if has_cycle(0,-1):
            return False


        return len(visited) == n
