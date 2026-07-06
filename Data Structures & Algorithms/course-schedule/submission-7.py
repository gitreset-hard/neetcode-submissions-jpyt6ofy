from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set() # cache
        path = set() # to detect cycle
        def hasCycle(crs):
            # cycle found
            if crs in path:
                return True
            
            # track curr path
            path.add(crs)

            for pre in graph[crs]:
                if hasCycle(pre):
                    return True

            visited.add(crs)
            path.remove(crs)
            return False


        for idx in range(numCourses):
            if idx not in visited:
                if hasCycle(idx):
                    return False
        
        return True

