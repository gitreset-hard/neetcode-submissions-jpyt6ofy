from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            0: [1, 2, 3]
            1: [4, 0]
            2: [0]
            3: [0]
            4: [1]
        """
        if len(edges) != n - 1:
            return False
            
        adjList = defaultdict(list)
        for x,y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        seen = set()
        seen.add(0)
        q = deque()
        q.append(0)
        valid = 0

        while q: # 2, 3, 4
            root = q.popleft()

            for neighbor in adjList[root]: 
                if neighbor not in seen: # 0, 1, 2, 3, 4
                    seen.add(neighbor)
                    q.append(neighbor)
                
                
            valid += 1

        return valid == n




