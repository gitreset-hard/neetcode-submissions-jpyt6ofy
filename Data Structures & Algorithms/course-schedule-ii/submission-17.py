from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        res = []
        currPath = set()
        visited = set() # mark safe after fully exploring


        def hasCycle(curr):
            # base case
            if curr in currPath:
                return True
            
            currPath.add(curr)
            for nei in graph[curr]:
                if hasCycle(nei):
                    return True
            
            currPath.remove(curr)
            if curr not in visited:
                res.append(curr)
            visited.add(curr)
            return False

                

        for idx in range(numCourses):
            if hasCycle(idx):
                return []
        
        return res