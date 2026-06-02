from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            - directed graph
            - if cycle -> False
            - possible to have no pre-reqs so we can't do:
                if n - 1 != len(prerequisites):
                    return False
            - start dfs from to verify cycle check 0 -> numCourses -1
        """
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        cur_path = set()
        visited = set() # gobal
        def dfs(crs):
            if crs in visited:
                return True

            if crs in cur_path:
                return False
            cur_path.add(crs)

            for neighbor in graph[crs]:
                if not dfs(neighbor):
                    return False
            
            cur_path.remove(crs)
            visited.add(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
